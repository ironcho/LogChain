from MainController import Property
from Network import Sender
import json

def Send_Block_Confirm():

    Confirm = {'To': 'cloud_peer', 'from': Property.my_ip_address, 'type': 'C'}
    jsonString = json.dumps(Confirm)
    Sender.send(Property.Cloud_Peer,jsonString,Property.port)