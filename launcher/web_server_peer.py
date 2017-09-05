import threading
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication.p2p import receiver
from communication.p2p import node_mapping_table

from service.blockmanager import genesisblock


def main():
    'Remove all transaction in mempool'
    # file_controller.remove_all_transactions()
    print("Web Server Start")

    'Peer setting'
    my_ip_address = file_controller.get_my_ip()
    nodeproperty.my_ip_address = my_ip_address
    set_peer.set_peer()
    print("my peer : " + str(nodeproperty.my_peer_num))

    'receiver thread start'
    print("Peer Start. Peer num : " + str(nodeproperty.my_peer_num))

    node_mapping_table.initialize()
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.my_ip_address, nodeproperty.REST_node_port)
    recv_thread.start()
    print("REST API RECEIVER START")

    print("tete")


if __name__ == '__main__':
    main()
