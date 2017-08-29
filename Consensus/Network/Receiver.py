from socket import *
from StorageManager import FileController
import json

def start(thread_name, ip_address, port):

    print 'receiver thread start'
    addr = (ip_address, port)
    buf_size = 8000

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(addr)
    tcp_socket.listen(1)

    while True:
        receive_socket, sender_ip = tcp_socket.accept()
        try:
            while True:

                data = receive_socket.recv(buf_size)
                #print "Receiving " + data
                data_entity = json.loads(data)

                if data_entity['type'] == 't':
                    FileController.add_transaction(data)
                    receive_socket.close()
                    break

                elif data_entity['type'] == 'B':
                    FileController.create_new_block(str(data_entity['block_height']), data)
                    receive_socket.close()
                    break

                elif data_entity['type'] == 'V':
                    FileController.add_voting(data)
                    receive_socket.close()
                    break
                elif data_entity['type'] == 'C':
                    FileController.add_blockconfirm(data)
                    receive_socket.close()
                    break
                else:
                    print "No data in socket"
                    break

        except Exception as e:
            print "Exception ", e
            break

    tcp_socket.close()


