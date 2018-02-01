import logging
import platform
from peerproperty import nodeproperty
from storage import file_controller
from communication.peermgr import peermgr

def init_myIP():
    logging.info("Set the peer's own IP address.")
    os = platform.system()
    if os is 'Linux':
        logging.info("peer's os is Linux.")
        # For raspberry pi, we use wlan,
        # so we need to figure out the IP address in a different way.
        nodeproperty.My_IP_address = file_controller.get_my_ip_rpi()
    elif os is 'Windows':
        logging.info("peer's os is Windows.")
        nodeproperty.My_IP_address = file_controller.get_my_ip()



def set_peer():
    if nodeproperty.My_IP_address==None:
        init_myIP()

    if nodeproperty.My_IP_address == nodeproperty.Peer1:
        nodeproperty.My_peer_num = 1
    elif nodeproperty.My_IP_address == nodeproperty.Peer2:
        nodeproperty.My_peer_num = 2
    elif nodeproperty.My_IP_address == nodeproperty.Peer3:
        nodeproperty.My_peer_num = 3
    elif nodeproperty.My_IP_address == nodeproperty.Peer4:
        nodeproperty.My_peer_num = 4
    # elif nodeproperty.my_ip_address == nodeproperty.Peer5:
    #     nodeproperty.my_peer_num = 5
    # elif nodeproperty.my_ip_address == nodeproperty.Peer6:
    #     nodeproperty.my_peer_num = 6
    # elif nodeproperty.my_ip_address == nodeproperty.Peer7:
    #     nodeproperty.my_peer_num = 7
    # elif nodeproperty.my_ip_address == nodeproperty.Peer8:
    #     nodeproperty.my_peer_num = 8
    # elif nodeproperty.my_ip_address == nodeproperty.Peer9:
    #     nodeproperty.my_peer_num = 9
    else:
        nodeproperty.My_peer_num = "API_Peer"


def set_my_peer_num():
    if nodeproperty.My_IP_address == None :
        init_myIP()
    p_num = 0
    for i in peermgr.ConnectedPeerList :
        if i[1] == nodeproperty.My_IP_address:
            nodeproperty.My_peer_num = p_num
        else:
            p_num = p_num  + 1


