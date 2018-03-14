import threading
import logging
from queue import Queue
import time
import json
from service.transactionmanager import transaction
from storage import file_controller
from service.blockconsensus import merkle_tree
from service.blockconsensus import voting
from monitoring import monitoring
from communication.peermgr import peerconnector


class TransactionTypeQueueThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_inq, p_socket_inq):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.inq = p_inq
        self.socketq = p_socket_inq

    def run(self):
        receive_event(self.thrd_name, self.inq, self.socketq)


def receive_event(p_thrd_name, p_inq, p_socketq):
    transaction_count = 0
    while True:
        # Wait for the Tx to be included in the block through a new consensus session.
        # PeerConnector updates ConnectedPeerList before collecting new Txs.
        # PeerMgr ...?

        peerconnector.connect_to_peermgr()

        monitoring.log("log.Waiting for T type msg.")
        recv_data = p_inq.get()
        request_sock = p_socketq.get()
        monitoring.log("log.T type msg rcvd: " + recv_data)
        transaction_count = transaction_count + 1

        file_controller.add_transaction(recv_data)
        monitoring.log("log.Transaction added to mempool: " + recv_data)

        # transaction_count = len(file_controller.get_transaction_list())

        if transaction_count == voting.TransactionCountForConsensus:

            difficulty = 0

            transaction.Transactions = file_controller.get_transaction_list()

            merkle = merkle_tree.MerkleTree()
            transaction.Merkle_root = merkle.get_merkle(
                transaction.Transactions)
            monitoring.log(
                "log.Transaction list Merkle _root: " + transaction.Merkle_root)

            monitoring.log("log.Start blind voting")
            voting.blind_voting(transaction.Merkle_root)
            monitoring.log("log.End voting")

            '''
            time.sleep(5)

            difficulty = voting.result_voting()

            file_controller.remove_all_voting()
            if(difficulty > 0):
                block_generator.generate_block(
                    difficulty, merkle_root, transactions)
            else :
                print("Wait block")


            file_controller.remove_all_transactions()
            '''
            transaction_count = 0

        request_sock.close()
