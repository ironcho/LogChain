
import threading
import logging
import sys
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication.p2p import node_mapping_table
from restapi_dispatch import query_block_queue
from restapi_dispatch import save_tx_queue
from queue import Queue

app = Flask(__name__)

query_q = Queue()
savetx_q = Queue()


rulelist = [
    {
        'id': 1,
        'title': u'Buy',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


def initialize_blockdbinfo():
    logging.info('Remove all transactions in mempool')
    file_controller.remove_all_transactions()
    # file_controller.remove_all_Block()
    logging.info('Remove all voting info ')
    file_controller.remove_all_voting()


def initialize_netinfo():
    nodeproperty.my_ip_address = file_controller.get_my_ip()
    set_peer.set_peer()
    logging.info("my peer : " + nodeproperty.my_peer_num)

    # node_mapping_table.set_node()와 set_peer()는 중복 기능이나, 일단 디버깅용으로 중복으로 유지함
    node_mapping_table.set_node()


@app.route('/rules/', methods=['GET'])
def get_rules():
    logging.debug('request(query rulelist) rcvd...')
    query_q.put("rulelist")
    logging.debug(str(query_q))
    logging.debug(query_q.qsize())
    return jsonify({'rulelist': rulelist})


@app.route('/rules/<int:rule_id>', methods=['GET'])
def get_rule(rule_id):
    logging.debug('request(query rule) rcvd...')
    query_q.put("rule_id")
    logging.debug(str(query_q))
    logging.debug(query_q.qsize())
    return jsonify({'rule': rule_id})


@app.route('/rules/', methods=['POST'])
def create_rule():
    logging.debug('request(create rule) rcvd...')
    logging.debug('event-> queue')
    savetx_q.put(request.json)
    logging.debug(str(savetx_q))
    logging.debug(savetx_q.qsize())

    # for testing......
    if not request.json or not 'title' in request.json:
        abort(400)
    rule = {
        'id': rulelist[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    rulelist.append(rule)
    # ...........for testing
    return jsonify({'rule': rule}), 201


@app.route("/")
def hello():
    return "LogChain's REST API node"


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    initialize_blockdbinfo()
    initialize_netinfo()

    logging.debug('QueryQueueThread starts')
    queryqueue_thread = query_block_queue.QueryQueueThread(
        1, "QueryQueueThread", query_q
    )
    queryqueue_thread.start()
    logging.debug('QueryQueueThread started')

    logging.debug('SaveTxQueueThread starts')
    savetxqueue_thread = save_tx_queue.SaveTxQueueThread(
        1, "SaveTxQueueThread", savetx_q
    )
    savetxqueue_thread.start()
    logging.debug('SaveTxQueueThread started')

    app.run()
