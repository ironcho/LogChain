import threading
import logging
from queue import Queue
import time
import json
from service.transactionmanager import transaction
from storage import file_controller
from service.blockconsensus import merkle_tree
from service.blockconsensus import voting


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
        logging.debug("Waiting for T type msg.")
        recv_data = p_inq.get()
        request_sock = p_socketq.get()

        logging.debug("Transaction received")
        transaction_count = transaction_count + 1
        # print(transaction_count)

        file_controller.add_transaction(recv_data)
        logging.debug("Transaction added to mempool: "+ recv_data)

        # transaction_count = len(file_controller.get_transaction_list())
        # print(transaction_count)
        if transaction_count == 30:
            #print ("Enter transaciotn count")
            difficulty = 0

            transaction.Transactions = file_controller.get_transaction_list()

            merkle = merkle_tree.MerkleTree()
            transaction.Merkle_root = merkle.get_merkle(
                transaction.Transactions)
            logging.debug("Transaction list Merkle _root: "+ transaction.Merkle_root)


            'blind voting'
            logging.debug("Start blind voting")
            voting.blind_voting(transaction.Merkle_root)
            logging.debug("End voting")


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
