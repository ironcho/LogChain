from peerproperty import nodeproperty
from storage import file_controller


def set_peer():
    my_ip = file_controller.get_my_ip()
    if my_ip == nodeproperty.Peer1:
        nodeproperty.my_peer_num = 1
    elif my_ip == nodeproperty.Peer2:
        nodeproperty.my_peer_num = 2
    elif my_ip == nodeproperty.Peer3:
        nodeproperty.my_peer_num = 3
    else:
        nodeproperty.my_peer_num = "API_Peer"
