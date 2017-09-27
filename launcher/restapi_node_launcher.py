import threading
import time
import json
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from service.transactionmanager import transaction
from communication.p2p import receiver
from communication.p2p import sender
from communication.p2p import node_mapping_table
import logging
import sys

from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

app = Flask(__name__)


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


def initialize_node():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logging.debug('A debug message!')
    logging.info('REST API server starts...')

    logging.info('Peer setting...')
    nodeproperty.my_ip_address = file_controller.get_my_ip()
    set_peer.set_peer()
    logging.info("my peer : " + nodeproperty.my_peer_num)

    # node_mapping_table.set_node()와 set_peer()는 중복 기능이나, 일단 디버깅용으로 중복으로 유지함
    node_mapping_table.set_node()

    logging.info('save_tx_queue thread starts')

    logging.info('query_block_queue thread starts')


def initiate_blockinfo():
    'Remove all transaction in mempool'
    file_controller.remove_all_transactions()
    # file_controller.remove_all_Block()
    file_controller.remove_all_voting()


@app.route('/rulelist/', methods=['GET'])
def get_rules():
    return jsonify({'rulelist': rulelist})


@app.route('/rules/', methods=['POST'])
def create_rule():
    logging.debug('create rule evbet dvf!')

    if not request.json or not 'title' in request.json:
        abort(400)
    rule = {
        'id': rulelist[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    rulelist.append(rule)
    return jsonify({'rule': rule}), 201


@app.route("/")
def hello():
    return "LogChain's REST API node!"


if __name__ == "__main__":
    initialize_node()
    app.run()
