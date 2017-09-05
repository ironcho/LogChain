import threading
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication import receiver
from service.blockmanager import genesisblock
from storage import file_controller


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
    threading._start_new_thread(receiver.start(
        "Receiver", my_ip_address, nodeproperty.port))

    print("tete")


if __name__ == '__main__':
    main()
