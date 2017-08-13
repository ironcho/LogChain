#precondition : Receiver is activated
from socket import *
import NodeMappingTable
import Property
# port num이나 이런 것들은 추후에 계속 정해야 한다. 현재는 같은 네트워크 망 안에서 있을 때만 통신이 가능..
def sending_tx():
    #need make transaction call

    f = open("transaction_new0.txt", 'r')
    transaction = f.read()

    send_to_all(transaction)
    #Property.tx_count += 1
    f.close()
def sending_mining_block():
    #need make block call
    f = open("block0.txt", 'r')
    block = f.read()
    send_to_all(block)

def sending_connection(p_ip):
    msg = "new node"
    send(p_ip, msg, Property.port)

def send(p_ip, p_msg, p_port, *args):


    if p_ip == Property.my_node.self_node:
        #print "Error"
        receiver_addr = (p_ip, p_port)

        tcp_socket = socket(AF_INET, SOCK_STREAM)

        try:
            tcp_socket.connect(receiver_addr)
            tcp_socket.settimeout(2)
            tcp_socket.send(p_msg.encode("utf-8"))

        except Exception as e:
            print (e)

        tcp_socket.close()
    else:
        receiver_addr = (p_ip, p_port)
        tcp_socket = socket(AF_INET, SOCK_STREAM)
        print("receiver addr =" + str(p_ip) + " , "+str(p_port))
        try:
            tcp_socket.connect(receiver_addr)
            tcp_socket.settimeout(2)
            tcp_socket.send(p_msg.encode("utf-8"))

        except Exception as e:
            print (e)

        tcp_socket.close()
    print("Sending complete")

def send_to_all(p_msg):

    #Property.my_node.print_table()

    for connected_node in Property.my_node.linked_node :
        send(connected_node, p_msg, Property.port)
