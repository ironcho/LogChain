import random
import json
import time

from storage import file_controller
from peerproperty import nodeproperty

from service.blockmanager import block
from service.blockconsensus import proof_of_work
from communication.p2p import sender


def generate_block(difficulty, merkle_root, transactions):

    try:
        'set block header info'
        print("=================================")
        print("Generate Block")

        start_time = time.time()


        prev_block_height, prev_hash = file_controller.get_last_block()
        block_info = merkle_root + prev_hash
        vote_result = difficulty

        'mining block'
        block_hash, nonce, tryanderror = proof_of_work.proof_of_work(
            block_info, difficulty)
        timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())


        'create block header'
        block_header = block.BlockHeader(
            prev_hash, nonce, merkle_root, vote_result, timestamp)
        block_header.block_id = "test_block_id"
        block_header.block_number = int(prev_block_height) + 1
        block_header.block_hash = block_hash
        block_header.block_info = block_info
        block_header.miner = nodeproperty.peer_num
        block_header.num_tx = len(transactions)


        'create block'
        new_block = block.Block(block_header, transactions)
        json_new_block = json.dumps(
            new_block, indent=4, default=lambda o: o.__dict__, sort_keys=True)
        print("Generate block complete")
        print(" ")

        end_time = time.time()
        elapsed_time = end_time - start_time

        print("Block Generate Time Time: %.4f seconds" % elapsed_time)
        print("   ")

        print("")

        sender.send_to_all(json_new_block)
        print("send block complete")
        print("Transaction per second", 30/elapsed_time)

    except TypeError as te:
        print("@generate block", te)



'''
if __name__ == '__main__':
    generate_block(11)
'''