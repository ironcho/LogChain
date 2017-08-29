from MainController import Property
from StorageManager import FileController
from Network import Sender
import json

def Send_Vote(vote_number):

    Peernumber = vote_number
    Voting = {'To': vote_number,'from':Property.my_ip_address,'type':'V'}
    jsonString =json.dumps(Voting)

    if Property.my_peer_num == Peernumber:
        FileController.add_voting(jsonString)
    else:
        if Peernumber == 1:
            ip_address = Property.Peer1
            Sender.send(ip_address,jsonString,Property.port)
        elif Peernumber == 2:
            ip_address = Property.Peer2
            Sender.send(ip_address,jsonString,Property.port)
        elif Peernumber == 3:
            ip_address = Property.Peer3
            Sender.send(ip_address,jsonString,Property.port)
        elif Peernumber == 4:
            ip_address = Property.Peer4
            Sender.send(ip_address,jsonString,Property.port)
        elif Peernumber == 5:
            ip_address = Property.Peer5
            Sender.send(ip_address,jsonString,Property.port)
        elif Peernumber == 6:
            ip_address = Property.Peer6
            Sender.send(ip_address,jsonString,Property.port)