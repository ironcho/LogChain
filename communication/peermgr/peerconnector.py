import threading
import logging
import json
import time
from queue import Queue


with open('peermgr.json', 'r') as f:
    config = json.load(f)

peerconnector_id = config['PEER_CONNECTOR']['ID']
peerconnector_ip = config['PEER_CONNECTOR']['IP']
peerconnector_port = config['PEER_CONNECTOR']['PORT']
