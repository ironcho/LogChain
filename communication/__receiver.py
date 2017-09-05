from socket import *
from storage import file_controller
from service.blockconsensus import voting
from service.blockconsensus import merkle_tree
from service.blockconsensus import block_generator
import json

def start(thread_name, ip_address, port):

    print ('receiver thread start')
    addr = (ip_address, port)
    buf_size = 10000

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(addr)
    tcp_socket.listen(1)

    while True:
        receive_socket, sender_ip = tcp_socket.accept()
        try:
            while True:
                data = receive_socket.recv(buf_size)
                print ("Receiving " + data)
                data_entity = json.loads(data)

                if data_entity['type'] == 't':
                    file_controller.add_transaction(data)

                    transaction_count = len(file_controller.get_transaction_list())
                    if transaction_count==10:

                        difficulty =0
                        transactions = file_controller.get_transaction_list()
                        merkle = merkle_tree.MerkleTree()
                        merkle_root = merkle.get_merkle(transactions)

                        'blind voting'
                        voting.bling_voting(merkle_root)
                        difficulty = voting.result_voting()

                        if(difficulty>0):
                            block_generator.generate_block(difficulty, merkle_root,transactions)

                    receive_socket.close()
                    file_controller.remove_all_transactions()
                    break

                elif data_entity['type'] == 'B':
                    file_controller.create_new_block(str(data_entity['block_height']), data)
                    receive_socket.close()
                    break

                elif data_entity['type'] == 'V':
                    file_controller.add_voting(data)
                    receive_socket.close()
                    break
                elif data_entity['type'] == 'C':
                    file_controller.add_blockconfirm(data)
                    receive_socket.close()
                    break
                else:
                    print ("No data in socket")
                    print(2)
                    break

        except Exception as e:
            print ("Exception ", e)
            break

    tcp_socket.close()


