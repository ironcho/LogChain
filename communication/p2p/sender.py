#precondition : Receiver is activated
from socket import *
from communication.p2p import node_mapping_table
from storage import file_controller

from peerproperty import nodeproperty
# port num이나 이런 것들은 추후에 계속 정해야 한다. 현재는 같은 네트워크 망 안에서 있을 때만 통신이 가능..

import json


def sending_tx():
    # need make transaction call

    f = open("transaction_new0.txt", 'r')
    transaction = f.read()

    send_to_all(transaction)
    #Property.tx_count += 1
    f.close()


def sending_mining_block():
    # need make block call
    f = open("block0.txt", 'r')
    block = f.read()
    send_to_all(block)


def sending_connection(p_ip):
    msg = "new node"
    send(p_ip, msg, nodeproperty.port)


def send(p_ip, p_msg, p_port, *args):

    if p_ip == nodeproperty.my_node.self_node:
        # print "Error"
        receiver_addr = (p_ip, p_port)

        tcp_socket = socket(AF_INET, SOCK_STREAM)

        try:

            tcp_socket.connect(receiver_addr)
            tcp_socket.settimeout(2)
            tcp_socket.send(p_msg.encode('utf-8'))

        except Exception as e:
            print(e)

        tcp_socket.close()

    else:
        receiver_addr = (p_ip, p_port)
        tcp_socket = socket(AF_INET, SOCK_STREAM)
        print("receiver addr =" + str(p_ip) + " , " + str(p_port))
        try:
            tcp_socket.connect(receiver_addr)
            print("connected........")
            tcp_socket.settimeout(2)
            print(p_msg)
            tcp_socket.send(p_msg.encode('utf-8'))
            print("end send")
        except Exception as e:
            print(e)

        tcp_socket.close()

    print("Sending complete")


def send_to_all(p_msg):

    # Property.my_node.print_table()

    for connected_node in nodeproperty.my_node.linked_node:
        send(connected_node, p_msg, nodeproperty.port)


def send_to_all_node(message, my_ip, my_port):

    address_list = file_controller.get_ip_list()
    for addr in address_list:
        try:
            send(addr, message, my_port)
        except Exception as e:
            print(e)
    print('send block')
