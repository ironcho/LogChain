from peerproperty import nodeproperty
from storage import file_controller
from communication import sender
import json


def blind_voting(merkle_root):

    vote_number = (int(merkle_root, 16) % nodeproperty.peer_num) + 1
    voting = {'To': vote_number,
              'from': nodeproperty.my_ip_address, 'type': 'V'}
    jsonString = json.dumps(voting)

    if nodeproperty.my_peer_num == vote_number:
        file_controller.add_voting(jsonString)
    else:
        if vote_number == 1:
            ip_address = nodeproperty.Peer1
            sender.send(ip_address, jsonString, nodeproperty.port)
        elif vote_number == 2:
            ip_address = nodeproperty.Peer2
            sender.send(ip_address, jsonString, nodeproperty.port)
        elif vote_number == 3:
            ip_address = nodeproperty.Peer2
            sender.send(ip_address, jsonString, nodeproperty.port)
        elif vote_number == 4:
            ip_address = nodeproperty.Peer2
            sender.send(ip_address, jsonString, nodeproperty.port)


def result_voting():
    list = file_controller.get_voting_list()

    if len(list) == 1:
        difficulty = 23
        return difficulty
    elif len(list) == 2:
        difficulty = 19
        return difficulty
    elif len(list) == 3:
        difficulty = 15
        return difficulty
    elif len(list) == 4:
        difficulty = 11

    return difficulty
