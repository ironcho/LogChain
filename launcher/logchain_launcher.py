import threading
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication.p2p import receiver
from communication.p2p import node_mapping_table
from service.blockmanager import genesisblock


def main():
    'Remove all transaction in mempool'
    file_controller.remove_all_transactions()
    print("Logchain Start")

    'Peer setting'
    my_ip_address = file_controller.get_my_ip()
    nodeproperty.my_ip_address = my_ip_address
    set_peer.set_peer()
    print("my peer num : " + str(nodeproperty.my_peer_num))

    # node_mapping_table.set_node()와 set_peer()는 중복 기능이나, 일단 디버깅용으로 중복으로 유지함
    node_mapping_table.set_node()

    'Genesis Block Create'
    genesisblock.genesisblock_generate()

    'receiver thread start'
    print("Peer Start. Peer num : " + str(nodeproperty.my_peer_num))

    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.my_ip_address, nodeproperty.port)
    recv_thread.start()
    print("RECEIVER START")


'''
    threading._start_new_thread(receiver.start(
        "Receiver", my_ip_address, nodeproperty.port))
'''


if __name__ == '__main__':
    main()
