import threading
from peerproperty import property
from peerproperty import set_peer
from storage import file_controller
from communication import receiver


def main():
    'Remove all transaction in mempool'
    file_controller.remove_all_transactions()

    'Peer setting'
    my_ip_address = file_controller.get_my_ip()
    property.my_ip_address = my_ip_address
    set_peer.set_peer()
    print("my peer : " + str(property.my_peer_num))

    'reveiver thread start'
    threading._start_new_thread(receiver.start(
        "Receiver", my_ip_address, property.port))
    print("RECEIVER START")


if __name__ == '__main__':
    main()
