from peerproperty import nodeproperty
from storage import file_controller


def set_peer():

    # my_ip = file_controller.get_my_ip()
    if nodeproperty.my_ip_address == nodeproperty.Peer1:
        nodeproperty.my_peer_num = 1
    elif nodeproperty.my_ip_address == nodeproperty.Peer2:
        nodeproperty.my_peer_num = 2
    elif nodeproperty.my_ip_address == nodeproperty.Peer3:
        nodeproperty.my_peer_num = 3
    elif nodeproperty.my_ip_address == nodeproperty.Peer4:
        nodeproperty.my_peer_num = 4
    else:
        nodeproperty.my_peer_num = "API_Peer"
