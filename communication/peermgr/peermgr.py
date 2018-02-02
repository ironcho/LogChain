import threading
import logging
import json
import os
from queue import Queue
from socket import *
from communication.p2p import sender
from peerproperty import nodeproperty
from peerproperty import set_peer

with open(os.getcwd() + os.sep + "peermgr.json", 'r') as f:
    peermgr_config = json.load(f)

PeerMgr_ID = peermgr_config['PEER_MGR']['ID']
PeerMgr_IP = peermgr_config['PEER_MGR']['IP']
PeerMgr_Port = peermgr_config['PEER_MGR']['PORT']

# The peermgr configuration file(peermgr.json) contains only the ID list of peers.
# The IP list is not included.
Predefined_peer_list = peermgr_config['PEER_LIST']

# Since multiple PeerConnectors can attempt to connect to PeerMgr simultaneously,
# the request is processed asynchronously after enqueuing the request event
# to the queue Updating_NodeTable_q.
ConnectedPeer_rcvddata_q = Queue()
ConnectedPeer_socket_q = Queue()
ConnectedPeer_IP_q = Queue()

# Add PeerMgr information to ConnectedPeerList by default.
ConnectedPeerList = [[PeerMgr_ID, PeerMgr_IP]]


def start_peermgr() -> bool:
    if nodeproperty.My_IP_address != PeerMgr_IP :
        logging.debug('Only a node with a predefined IP can run PeerMgr.')
        return False


    logging.debug('Start listening thread to wait for connection of PeerConnector.')
    listening_to_peerconnector_thr = ListeningToPeerConnectorThread(
        1, "ListeningToPeerConnectorThread",
        PeerMgr_IP, PeerMgr_Port,
        ConnectedPeer_rcvddata_q, ConnectedPeer_socket_q, ConnectedPeer_IP_q
    )
    listening_to_peerconnector_thr.start()
    logging.debug('The listening thread is started to wait for the connection of PeerConnector.')


    logging.debug('Start a thread to manage ConnectedPeerList.')
    managing_peertable_thr = ManagingConnectedPeerListThread(
        1, "ManagingConnectedPeerListThread",
        Predefined_peer_list,
        ConnectedPeer_rcvddata_q, ConnectedPeer_socket_q, ConnectedPeer_IP_q
    )
    managing_peertable_thr.start()
    logging.debug('The thread to manage the ConnectedPeerList has started.')


    return True



class ListeningToPeerConnectorThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name,
                 p_ip, p_port,
                 p_inq, p_socketq, p_socketipq):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.p_ip = p_ip
        self.p_port = p_port
        self.thrd_name = p_thrd_name
        self.inq = p_inq
        self.socketq = p_socketq
        self.socketipq = p_socketipq


    def run(self):
        addr = (self.p_ip, self.p_port)
        buf_size = 100

        tcp_socket = socket(AF_INET, SOCK_STREAM)
        tcp_socket.bind(addr)
        tcp_socket.listen(5)
        while True:
            logging.debug('Wait for PeerConnector to connect.')
            request_sock, request_ip = tcp_socket.accept()
            logging.debug('PeerConnector connected.')

            while True:
                rcvd_total = []
                while True:
                    # Assuming the format of the incoming message is json
                    rcvd_pkt = request_sock.recv(buf_size)
                    if not rcvd_pkt:
                        break
                    rcvd_total.append(rcvd_pkt)
                rcvd_data = ""
                for i in rcvd_total:
                    rcvd_data += i.decode('utf-8')
                logging.debug("rcvd_data: " + rcvd_data)
                if rcvd_data == "":
                    break
                try:
                    self.inq.put(rcvd_data)
                    self.socketq.put(request_sock)
                    self.socketipq.put(request_ip)
                    break
                except Exception as e:
                    logging.debug(e)



class ManagingConnectedPeerListThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name,
                 p_peer_list,
                 p_inq, p_socketq, p_socketipq):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.peer_list = p_peer_list
        self.inq = p_inq
        self.socketq = p_socketq
        self.socketipq = p_socketipq


    def run(self):
        while True:
            rcvd_data = self.inq.get()
            request_sock = self.socketq.get()
            socketip = self.socketipq.get()

            # Assuming the format of the incoming message is json
            rcvd_data_json = json.loads(rcvd_data)
            peerid = rcvd_data_json['ID']
            logging.debug("The ID of ConnectedPeer: " + peerid)

            if peerid in self.peer_list:
                logging.debug("Add new peer's IP to ConnectedPeerList.")
                ConnectedPeerList.append([peerid,socketip])
                ConnectedPeerList.sort()
                request_sock.close()
                connected_peer_list_json = json.dumps(
                    ConnectedPeerList, indent=4, default=lambda o: o.__dict__, sort_keys=True)
                sender.send_to_all_peers(connected_peer_list_json)
                set_peer.set_my_peer_num()
                set_peer.set_total_peer_num()

            else:
                request_sock.close()
                # If there is no ID in the peer list, ignore it.
                logging.debug("Ignore it because there is no corresponding ID in the predefined list.")





# TODO: We should update ConnectedPeerList by periodically executing ping.










