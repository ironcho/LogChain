from socket import *
# import socket
import time
from StorageManager import FileController
from MainController import Property
#
# def get_my_ip():
#     ip = socket.gethostbyname(socket.gethostname())
#     return ip


def send(ip_address, message, port):
    receiver_addr = (ip_address, port)
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    try:
        tcp_socket.connect(receiver_addr)
        tcp_socket.send(message)
        #print "SEND COMPLETE"
    except Exception as e:
        print "connection failed", e
    tcp_socket.close()


def send_to_all_node(message, my_ip, my_port):

    address_list = FileController.get_ip_list()

    for addr in address_list:
        try:
            send(addr, message, my_port)
        except Exception as e:
                print e

