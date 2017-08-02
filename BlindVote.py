from BlockConsensusManager import Merkle
from BlockConsensusManager import PoW
from BlockConsensusManager import Block
import hashlib


class BlindVote(object):
    def __init__(self):
        pass

    @staticmethod
    def cal_candidate(total_node, merkle_root):

        delegated_node = (int(merkle_root, 16) % total_node) + 1
        return delegated_node

    @staticmethod
    def generate_block(prev_hash, total_node, vote_result, last_block, tx_list=[]):

        transactions = tx_list

        merkle_cls = Merkle.MerkleTree()
        merkle_root = merkle_cls.get_merkle(transactions)

        vote_rate = (vote_result/total_node)*100

        if vote_rate > 50:
            difficulty = 10000

        elif vote_rate < 50:
            difficulty = 100000

        else:
            difficulty = 10000

        current_nonce = PoW.proof_of_work(transactions, difficulty)

        block_header = Block.BlockHeader(prev_hash, current_nonce, merkle_root, vote_result)

        block_header.num_tx = len(tx_list)

        block_header_hash = hashlib.sha256(block_header).hexdigest()
        block_header.block_hash = block_header_hash

        block = Block.Block(block_header, tx_list)

        return block
