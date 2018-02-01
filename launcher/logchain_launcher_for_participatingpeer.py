import logging
import platform
import sys
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication.p2p import receiver
from communication.p2p import node_mapping_table
from service.blockmanager import genesisblock
from communication.msg_dispatch import dispatch_queue_list
from communication.msg_dispatch import t_type_queue_thread
from communication.msg_dispatch import b_type_queue_thread
from communication.msg_dispatch import v_type_queue_thread
from communication.peermgr import peerconnector


# Logchain launcher function for ParticipatingPeer
# ParticipatingPeer performs the role of PeerConnector in parallel.
def main():
    logging.basicConfig(stream = sys.stderr, level = logging.DEBUG)
    logging.debug('Start Logchain launcher for ParticipatingPeer...')

    logging.info('Start the blockchain-related initialization process...')
    file_controller.remove_all_transactions()
    file_controller.remove_all_blocks()
    file_controller.remove_all_voting()
    logging.info('Complete the initialization process...')

    logging.info('Set the peer\'s own IP address.')
    os = platform.system()
    if os is 'Linux':
        logging.info('peer\'s os is Linux.')
        # For raspberry pi, we use wlan,
        # so we need to figure out the IP address in a different way.
        nodeproperty.My_IP_address = file_controller.get_my_ip_rpi()
    elif os is 'Windows':
        logging.info('peer\'s os is Windows.')
        nodeproperty.My_IP_address = file_controller.get_my_ip()

    logging.info('Run processes for PeerConnector.')
    peerconnector.start_peerconnector()





    set_peer.set_peer()

    print("my peer num : " + str(nodeproperty.My_peer_num))
    print(" ")

    # node_mapping_table.set_node()와 set_peer()는 중복 기능이나, 일단 디버깅용으로 중복으로 유지함
    node_mapping_table.set_node()

    'Genesis Block Create'
    genesisblock.genesisblock_generate()

    'receiver thread start'
    print("Logchain Peer Start. Peer num : " + str(nodeproperty.My_peer_num))
    print(" ")

    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.My_IP_address, nodeproperty.port)
    recv_thread.start()
    #print("RECEIVER START")

    t_type_qt = t_type_queue_thread.TransactionTypeQueueThread(
        1, "TransactionTypeQueueThread",
        dispatch_queue_list.T_type_q,
        dispatch_queue_list.Connected_socket_q
    )
    t_type_qt.start()

    v_type_qt = v_type_queue_thread.VotingTypeQueueThread(
        1, "VotingTypeQueueThread",
        dispatch_queue_list.V_type_q,
        dispatch_queue_list.Connected_socket_q
    )
    v_type_qt.start()

    b_type_qt = b_type_queue_thread.BlockTypeQueueThread(
        1, "BlockTypeQueueThread",
        dispatch_queue_list.B_type_q,
        dispatch_queue_list.Connected_socket_q
    )
    b_type_qt.start()


'''
    threading._start_new_thread(receiver.start(
        "Receiver", my_ip_address, nodeproperty.port))
'''


if __name__ == '__main__':
    main()
