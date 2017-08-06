from socket import *
import Property
import threading
import json


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
        print ("Start Receiver Thread")
        receive_data(self.thrd_name, self.thrd_ip, self.thrd_port)


def receive_data(p_thrd_name, p_ip, p_port):
    """

    :param p_thrd_name:
    :param p_ip:
    :param p_port:
    :return:
    """

    addr = (p_ip, p_port)
    buf_size = 10000
    #to check my node info
    #print(p_thrd_name, p_ip, p_port)
    #
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(addr)
    tcp_socket.listen(5)
    num_tx =0
    num_block =0
    while True:
        print ("waiting")
        request_sock, request_ip = tcp_socket.accept()

        while True:
            #recv_data = request_sock.recv(buf_size)
            recv_data = request_sock.recv(buf_size).decode('utf-8')
            #print(recv_data)
            try:
                if recv_data == "":
                    break

                data_jobj = json.loads(recv_data)
                #print(data_jobj['type'])
                if data_jobj['type'] is 'T':
                    print ("Transaction received")

                    #받은 트랜잭션의 검증을 해야한다.

                    # 검증후 트랜잭션을 저장 해야함
                    #num_tx : tx의 로컬 인덱스를 항상 노드가 시작할때 체크를 해줘야 한다.
                    num_tx = num_tx + 1
                    #print(num_tx)
                    f = open("transaction_new" + str(num_tx) + ".txt", 'w')
                    f.write(recv_data)
                    f.close()
                    #일정량의 트랜잭션이 쌓였을 때 블록만들기 시작.

                elif data_jobj['type'] is 'B':
                    print ("Block received")

                    # block verification thread
                    #검증후 블록을 저장해야함
                    # num_block : block의 로컬 인덱스를 항상 노드가 시작할때 체크를 해줘야 한다.
                    num_block = num_block +1
                    #print(num_block)
                    f = open("block" + str(num_block) + ".txt", 'w')
                    f.write(recv_data)
                    f.close()
                    # remove all txs call

                #신규 노드 참여 통신은 완전 다르게 블록체인이 아닌 별도의 통신을 이용하면 더 좋을듯.
                '''elif data_jobj['type'] is 'N':
                    print ("new node connected")

                    node_list = FileController.get_ip_list()
                    received_ip = data_jobj['ip_address']

                    sync_flag = False

                    for outer_list in node_list:
                        outer_list = str(outer_list)
                        if outer_list == received_ip:
                            sync_flag = True

                    if sync_flag is False:
                        FileController.add_node(recv_data)'''

            except Exception as e:
                print ("SOCKET ERROR", e)
                break

    tcp_socket.close()
