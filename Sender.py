#precondition : Receiver is activated
from socket import *
import Property

def sending_tx():
    #need make transaction call
    #transaction이 만들어 지금 그것을 그냥 담아서 보내도 됨.
    f = open("transaction_new0.txt", 'r')
    transaction = f.read()

    send_to_all(transaction)
    #Property.tx_count += 1
    f.close()
def sending_mining_block():
    #need make block call
    #block이 만들어 지금 그것을 그냥 담아서 보내도 됨.
    f = open("block0.txt", 'r')
    block = f.read()
    Sender.send_to_all(block)


def send(p_ip, p_msg, p_port, *args):
    """
    Basic send function.
    Using TCP socket connection, send p_msg to (p_ip, p_port)

    :param p_ip: receiver's ip address
    :param p_msg: can be transaction, block, node information
    :param p_port: pre-defined port
    :param args: None

    :return: None
    """

    if p_ip == Property.my_ip:
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

        try:
            tcp_socket.connect(receiver_addr)
            tcp_socket.settimeout(2)
            tcp_socket.send(p_msg.encode("utf-8"))

        except Exception as e:
            print (e)

        tcp_socket.close()
    print("Sending complete")

def send_to_all(p_msg):
    """
    Send p_msg to all connected nodes
    implemented using send() function.

    :param p_msg: can be transaction, block, node information
    :return: None


    """
    #현재는 실험상 본인에게 보내는 것으로 코딩이 되어있음.
    send(Property.my_ip, p_msg, Property.port)
