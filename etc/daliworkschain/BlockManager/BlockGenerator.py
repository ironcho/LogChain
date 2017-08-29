import random
import json
from StorageManager import FileController
from MainController import Property
from Network import Sender
import hashlib
import hashlib


def generate_block(MerkleTree_Hash,my_port,my_ip_address,):
    from BlockManager import Block
    from StorageManager import FileController
    import json


    transactions = FileController.get_transaction_list()
    block_height,previous_blockhash, =FileController.get_last_block()
    block_info = MerkleTree_Hash +previous_blockhash
    block_hash = hashlib.sha256(str(block_info)).hexdigest()
    block_miner = Property.my_ip_address
    block_height = block_height+1

    block = Block.Block(block_hash, block_info, block_miner, block_height, MerkleTree_Hash, transactions,previous_blockhash)
    block_temp = json.dumps(block, indent=4, default=lambda o: o.__dict__, sort_keys=True)
    Sender.send_to_all_node(block_temp, my_ip_address, my_port)



