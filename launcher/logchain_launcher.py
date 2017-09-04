import threading
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication.p2p import receiver
from communication.p2p import node_mapping_table


def main():
    'Remove all transaction in mempool'
    file_controller.remove_all_transactions()

    'Peer setting'
    my_ip_address = file_controller.get_my_ip()
    nodeproperty.my_ip_address = my_ip_address
    set_peer.set_peer()
    print("my peer : " + str(nodeproperty.my_peer_num))

    'reveiver thread start'
    node_mapping_table.initialize()
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.my_ip_address, nodeproperty.port)
    recv_thread.start()
    print("RECEIVER START")


if __name__ == '__main__':
    main()
