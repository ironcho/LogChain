import threading
import json
import time
from socket import *
from peerproperty import nodeproperty
from storage import file_controller
from service.blockconsensus import merkle_tree
from service.blockconsensus import block_generator
from service.blockconsensus import voting


class ReceiverThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_ip, p_port):
        """

        :param p_thrd_id:
        :param p_thrd_name:
        :param p_ip:
        :param p_port:
        """
        threading.Thread.__init__(self)
        self.thrd_name = p_thrd_name
        self.thrd_id = p_thrd_id
        self.thrd_ip = p_ip
        self.thrd_port = p_port

    def run(self):
        #print("Start Receiver Thread")
        receive_data(self.thrd_name, self.thrd_ip, self.thrd_port)


def receive_data(p_thrd_name, p_ip, p_port):
    """

    :param p_thrd_name:
    :param p_ip:
    :param p_port:
    :return:
    """

    addr = (p_ip, p_port)
    buf_size = 100
    # to check my node info
    # print(p_thrd_name, p_ip, p_port)
    #
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(addr)
    tcp_socket.listen(5)
    transaction_count = 0
    num_block = 0
    while True:
        #print("waiting")
        request_sock, request_ip = tcp_socket.accept()

        while True:
            rcvd_total = []
            while True:
                rcvd_pkt = request_sock.recv(buf_size)
                if not rcvd_pkt : break
                rcvd_total.append(rcvd_pkt)

            temp = ""
            for i in rcvd_total:
                temp += i.decode('utf-8')

            recv_data = temp
            print("recv data: ")
            #print(recv_data)
            print("  ")

            if recv_data == "":
                break
            # print("from ip : " + str(request_ip[0]))
            # node mapping table 관리를 넣는다.
            if recv_data == "new node":
                if str(request_ip[0]) in nodeproperty.my_node.linked_node:
                    print("already connected")
                    break
                else:
                    print("new node connection received")
                    nodeproperty.my_node.table_add(
                        str(request_ip[0]), 'stable')
                    # Property.my_node.print_table()
                    nodeproperty.my_node.write_table()
                    break

                # 연결이 안되있는 노드로 부터 오는 메세지는 무시.
                '''
                print(recv_data)
                if str(request_ip[0]) not in nodeproperty.my_node.linked_node:
                    print("break??")
                    break
                '''

                # nodeproperty.my_node.table_update(str(request_ip[0]), 'true')
                # Property.my_node.print_table()
                # nodeproperty.my_node.write_table()
                # node mapping table 관리
            else:
                data_jobj = json.loads(recv_data)

                try:
                    if data_jobj['type'] is 'T':
                        print("  ")
                        print("Transaction received")
                        print("  ")
                        transaction_count = transaction_count + 1
                        #print(transaction_count)

                        file_controller.add_transaction(recv_data)
                        print("transaction added to mempool : ", recv_data)
                        print("  ")

                        # transaction_count = len(file_controller.get_transaction_list())
                        #print(transaction_count)
                        if transaction_count == 30:
                            #print ("Enter transaciotn count")
                            #difficulty = 0
                            transactions = file_controller.get_transaction_list()

                            merkle = merkle_tree.MerkleTree()
                            merkle_root = merkle.get_merkle(transactions)
                            print("Transaction list Merkle _root : ",merkle_root)
                            print(" ")
                            'blind voting'

                            print("Start blind voting")
                            voting.blind_voting(merkle_root)
                            print("  ")
                            print("End voting")
                            print("  ")

                            'time sleep-> result voting'
                            time.sleep(10)
                            difficulty = voting.result_voting()


                            file_controller.remove_all_voting()
                            if(difficulty > 0):
                                block_generator.generate_block(
                                    difficulty, merkle_root, transactions)
                            else :
                                print("Wait block")


                            file_controller.remove_all_transactions()
                            transaction_count =0

                        request_sock.close()
                        break

                except Exception as e:
                    print("Exception @receiver - data_jobj['type'] is 'T'", e)

                try:
                    if data_jobj['block_header']['type'] is 'B':
                        print("Block received")
                        # block verification thread

                        file_controller.create_new_block(
                            str(data_jobj['block_header']['block_number']), recv_data)

                        print("End create _new block")
                        request_sock.close()
                        break
                except Exception as e:
                    print("Exception @receiver - data_jobj['block_header']['type'] is 'B'", e)

                try:

                    if data_jobj['type'] is 'V':
                        print("Voting received")

                        # block verification thread

                        num_block = num_block + 1

                        file_controller.add_voting(recv_data)
                        request_sock.close()
                        break

                except Exception as e:
                    print("Exception @receiver - data_jobj['type'] is 'V'", e)
                        # remove all txs call

                try:
                    if data_jobj['type'] == 'C':
                        file_controller.add_blockconfirm(recv_data)
                        request_sock.close()
                        break

                except Exception as e:
                    print("Exception @receiver - data_jobj['type'] == 'C'", e)



                print("No data in socket")
                print(2)
                break

    tcp_socket.close()



