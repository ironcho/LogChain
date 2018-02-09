
import logging
import sys
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from queue import Queue
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from restapi_dispatch import query_block_queue
from restapi_dispatch import save_tx_queue
from communication.peermgr import peerconnector
from service.blockmanager import genesisblock
from communication.msg_dispatch import dispatch_queue_list
from communication.msg_dispatch import t_type_queue_thread
from communication.msg_dispatch import b_type_queue_thread
from communication.msg_dispatch import v_type_queue_thread
from communication.p2p import receiver
from monitoring import monitoring


app = Flask(__name__)

query_q = Queue()
savetx_q = Queue()


rulelist = [
    {
      "index": 1,
      "title": "Testing for MWC #1",
      "body": "abc"
    }
]


# def initialize_blockdbinfo():
#     logging.info('Remove all transactions in mempool')
#     file_controller.remove_all_transactions()
#     file_controller.remove_all_blocks()
#     logging.info('Remove all voting info ')
#     file_controller.remove_all_voting()


# def initialize_netinfo():
#     nodeproperty.My_IP_address = file_controller.get_my_ip()
#     set_peer.set_peer()
#     # logging.info("my peer : " + nodeproperty.my_peer_num)
#
#     # node_mapping_table.set_node()와 set_peer()는 중복 기능이나, 일단 디버깅용으로 중복으로 유지함
#     node_mapping_table.set_node()


@app.route('/rules/', methods=['GET'])
def get_rules():
    logging.debug('request(query rulelist) rcvd...')
    query_q.put("rulelist")
    logging.debug(str(query_q))
    logging.debug(query_q.qsize())
    return jsonify({'rulelist': rulelist})



@app.route('/rules/', methods=['POST'])
def create_rule():
    monitoring.log('log.request(create rule) rcvd...')
    savetx_q.put(request.json)
    monitoring.log("log."+str(savetx_q))
    monitoring.log("log."+str(savetx_q.qsize()))

    if not request.json or not 'title' in request.json:
        abort(400)
    rule = {
        'index': rulelist[-1]['index'] + 1,
        'title': request.json['title'],
        'body': request.json.get('body', "")
    }
    rulelist.append(rule)

    return jsonify({'rule': rule}), 201


@app.route("/")
def hello():
    return "LogChain launcher for Generic Peer - REST API node"


def initialize_process_for_generic_peer():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    monitoring.log("log.Start Logchain launcher for Generic Peer...")

    initialize()

    monitoring.log('log.Run processes for PeerConnector.')
    if not peerconnector.start_peerconnector():
        monitoring.log('log.Aborted because PeerConnector execution failed.')
        sys.exit(1)

    set_peer.set_my_peer_num()
    monitoring.log("log.My peer num: " + str(nodeproperty.My_peer_num))

    'Genesis Block Create'
    genesisblock.genesisblock_generate()

    monitoring.log("log.Start a thread to receive messages from other peers.")
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.My_IP_address, nodeproperty.My_receiver_port)
    recv_thread.start()
    monitoring.log("log.The thread for receiving messages from other peers has started.")


    t_type_qt = t_type_queue_thread.TransactionTypeQueueThread(
        1, "TransactionTypeQueueThread",
        dispatch_queue_list.T_type_q,
        dispatch_queue_list.Connected_socket_q
    )
    t_type_qt.start()

    v_type_qt = v_type_queue_thread.VotingTypeQueueThread(
        1, "VotingTypeQueueThread",
        dispatch_queue_list.V_type_q,
        dispatch_queue_list.Connected_socket_q
    )
    v_type_qt.start()

    b_type_qt = b_type_queue_thread.BlockTypeQueueThread(
        1, "BlockTypeQueueThread",
        dispatch_queue_list.B_type_q,
        dispatch_queue_list.Connected_socket_q
    )
    b_type_qt.start()


def initialize():
    monitoring.log('log.Start the blockchain initialization process...')
    file_controller.remove_all_transactions()
    file_controller.remove_all_blocks()
    file_controller.remove_all_voting()
    monitoring.log('log.Complete the blockchain initialization process...')
    set_peer.init_myIP()

def initialize_process_for_RESTAPInode():
    queryqueue_thread = query_block_queue.QueryQueueThread(
        1, "QueryQueueThread", query_q
    )
    queryqueue_thread.start()
    logging.debug('QueryQueueThread started')

    savetxqueue_thread = save_tx_queue.SaveTxQueueThread(
        1, "SaveTxQueueThread", savetx_q
    )
    savetxqueue_thread.start()
    logging.debug('SaveTxQueueThread started')


# REST API Node launcher function
if __name__ == "__main__":
    logging.basicConfig(stream = sys.stderr, level = logging.DEBUG)
    initialize_process_for_generic_peer()
    initialize_process_for_RESTAPInode()
    app.run(host='0.0.0.0')
