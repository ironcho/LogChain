from MainController import Property
from StorageManager import FileController


def Set_PeerNum():
    my_ip = FileController.get_my_ip()

    if my_ip == Property.peer_1:
        Property.my_peer_num = 1
    elif my_ip == Property.base_node_2:
        Property.my_peer_num = 2
    elif my_ip == Property.peer_3:
        Property.my_peer_num = 3
    elif my_ip == Property.base_node_4:
        Property.my_peer_num = 4
    elif my_ip == Property.peer_5:
        Property.my_peer_num = 5
    elif my_ip == Property.peer_6:
        Property.my_peer_num = 6
    else:
        Property.my_peer_num = 'cloud'
