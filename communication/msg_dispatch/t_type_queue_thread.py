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
        print("waiting for t type msg")
        recv_data = p_inq.get()
        request_sock = p_socketq.get()

        print("  ")
        print("Transaction received")
        print("  ")
        transaction_count = transaction_count + 1
        # print(transaction_count)

        file_controller.add_transaction(recv_data)
        print("transaction added to mempool : ", recv_data)
        print("  ")

        # transaction_count = len(file_controller.get_transaction_list())
        # print(transaction_count)
        if transaction_count == 30:
            #print ("Enter transaciotn count")
            difficulty = 0
            transactions = file_controller.get_transaction_list()

            merkle = merkle_tree.MerkleTree()
            merkle_root = merkle.get_merkle(transactions)
            print("Transaction list Merkle _root : ", merkle_root)
            print(" ")
            'blind voting'

            print("Start blind voting")
            voting.blind_voting(merkle_root)
            print("  ")
            print("End voting")
            print("  ")

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
