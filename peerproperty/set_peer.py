from peerproperty import property
from storage import file_controller

def set_peer():
    my_ip = file_controller.get_my_ip()
    if my_ip == property.Peer1:
        property.my_peer_num =1
    elif my_ip == property.Peer2:
        property.my_peer_num =2
    elif my_ip == property.Peer3:
        property.my_peer_num =3
    else:
        property.my_peer_num = "API_Peer"

