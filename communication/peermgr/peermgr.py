import threading
import logging
import json
import time
from queue import Queue


with open('peermgr.json', 'r') as f:
    config_peer = json.load(f)

peermgr_id = config_peer['PEER_MGR']['ID']
peermgr_ip = config_peer['PEER_MGR']['IP']
peermgr_port = config_peer['PEER_MGR']['PORT']

peer_id_array = config_peer['PEER_ID_LIST']


def main():
    peer_updating_q = Queue()
    peermgr_listening_thread = PeerMgrListeningThread(
        1, "PeerMgrListeningThread", peermgr_ip, nodeproperty.peermgr_port, peer_updating_q
    )
    peermgr_listening_thread.start()
    logging.debug('PeerMgrListeningThread started')

    peermgr_nodetableupdate_thread = PeerMgrUpdatingNodeTableThread(
        1, "PeerMgrUpdatingNodeTableThread", peer_updating_q
    )
    peermgr_nodetableupdate_thread.start()
    logging.debug('PeerMgrUpdatingNodeTableThread started')


class PeerMgrListeningThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_ip, p_port, p_inq):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.inq = p_inq

    def run(self):
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
            print("waiting for connection ")
            request_sock, request_ip = tcp_socket.accept()

            while True:
                rcvd_total = []
                while True:
                    rcvd_pkt = request_sock.recv(buf_size)
                    if not rcvd_pkt:
                        break
                    rcvd_total.append(rcvd_pkt)

                temp = ""
                for i in rcvd_total:
                    temp += i.decode('utf-8')

                recv_data = temp
                print("recv data: ")
                # print(recv_data)
                print("  ")

                if recv_data == "":
                    break
                # print("from ip : " + str(request_ip[0]))
                # node mapping table 관리를 넣는다.


class PeerMgrUpdatingNodeTableThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_inq):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.inq = p_inq

    def run(self):
        receive_event(self.thrd_name, self.inq)


def receive_event(p_thrd_name, p_inq):
    count = 1
    while True:
        logging.debug("waiting for peer connection event")

        dequeued = p_inq.get()

        tx = transaction.Transaction(dequeued)
        temp = json.dumps(
            tx, indent=4, default=lambda o: o.__dict__, sort_keys=True)

        sender.send_to_all(temp)  # 노드들 연동 후 테스트 필요 2017-09-27

        logging.debug(str(dequeued))
        logging.debug(str(temp))

        logging.debug(count)
        logging.debug(str(p_inq.qsize()))
        count = count + 1
        time.sleep(queue_strategy.SAVE_TX_DEQUEUE_INTERVAL)


if __name__ == '__main__':
    main()
