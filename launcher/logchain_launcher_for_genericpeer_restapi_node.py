
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


app = Flask(__name__)

query_q = Queue()
savetx_q = Queue()


rulelist = [
    {
        'index': 1,
        'title': 'Testing-rule #1',
        'body': {
            "conditions": [
                []
            ],
            "actions": [
                [
                    {
                        "agent": "actuator",
                        "type": "led",
                        "method": {
                            "name": "LED 제어",
                            "id": "led",
                            "params": {
                                "command": {
                                    "cmd": "blink",
                                    "options": {
                                        "duration": 7000,
                                        "interval": 1500
                                    }
                                },
                                "notificationOption": "Failure",
                                "target": {
                                    "type": "gateway",
                                    "id": "b827ebda7b2a",
                                    "sensors": [
                                        "b827ebda7b2a-0-led"
                                    ]
                                }
                            }
                        }
                    }
                ]
            ],
            "severity": "information",
            "timezone": "+9.00",
            "name": "buttonLED700",
            "status": "activated",
            "trigger": {
                "agent": "sensorValue",
                "type": "onoff",
                "method": {
                    "name": "변경",
                    "id": "changed",
                    "params": {
                        "from": "0",
                        "to": "1",
                        "target": {
                            "type": "tag",
                            "id": "1",
                            "sensors": [
                                "b827ebda7b2a-0-button"
                            ]
                        }
                    }
                },
                "filter": {
                    "type": [
                        "series"
                    ],
                    "gateway": "*",
                    "sensor": [
                        "b827ebda7b2a-0-button"
                    ]
                }
            }
        }
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
    logging.debug('request(create rule) rcvd...')
    savetx_q.put(request.json)
    logging.debug(str(savetx_q))
    logging.debug(savetx_q.qsize())

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
    logging.info("Start Logchain launcher for Generic Peer...")

    initialize()

    logging.info('Run processes for PeerConnector.')
    if not peerconnector.start_peerconnector():
        logging.info('Aborted because PeerConnector execution failed.')
        return

    set_peer.set_my_peer_num()
    logging.info("My peer num: " + str(nodeproperty.My_peer_num))

    'Genesis Block Create'
    genesisblock.genesisblock_generate()

    logging.info("Start a thread to receive messages from other peers.")
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.My_IP_address, nodeproperty.My_receiver_port)
    recv_thread.start()
    logging.info("The thread for receiving messages from other peers has started.")


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
    logging.info('Start the blockchain initialization process...')
    file_controller.remove_all_transactions()
    file_controller.remove_all_blocks()
    file_controller.remove_all_voting()
    logging.info('Complete the blockchain initialization process...')
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
    app.run()
