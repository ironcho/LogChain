import threading
import logging
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication.p2p import receiver
from communication.p2p import node_mapping_table
from service.blockmanager import genesisblock

from communication.msg_dispatch import dispatch_queue
from communication.msg_dispatch import t_type_queue
from communication.msg_dispatch import b_type_queue
from communication.msg_dispatch import v_type_queue


def main():
    'Remove all transaction in mempool'
    file_controller.remove_all_transactions()
    # file_controller.remove_all_Block()
    file_controller.remove_all_voting()

    print("==Log Chain Start==")
    print(" ")
    'Peer setting'
    nodeproperty.my_ip_address = file_controller.get_my_ip()
    set_peer.set_peer()

    print("my peer num : " + str(nodeproperty.my_peer_num))
    print(" ")

    # node_mapping_table.set_node()와 set_peer()는 중복 기능이나, 일단 디버깅용으로 중복으로 유지함
    node_mapping_table.set_node()

    'Genesis Block Create'
    genesisblock.genesisblock_generate()

    'receiver thread start'
    print("Logchain Peer Start. Peer num : " + str(nodeproperty.my_peer_num))
    print(" ")

    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.my_ip_address, nodeproperty.port)
    recv_thread.start()
    #print("RECEIVER START")

    t_type_queue_thread = t_type_queue.TransactionTypeQueueThread(
        1, "TransactionTypeQueueThread", dispatch_queue.T_type_q, dispatch_queue.Connected_socket_q
    )
    t_type_queue_thread.start()


'''
    threading._start_new_thread(receiver.start(
        "Receiver", my_ip_address, nodeproperty.port))
'''


if __name__ == '__main__':
    main()
