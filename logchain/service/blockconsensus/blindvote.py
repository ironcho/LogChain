from blockconsensus import merkle
from blockconsensus import proof_of_work
from blockmanager import block


class BlindVote(object):
    def __init__(self):
        pass

    @staticmethod
    def cal_candidate(total_node, merkle_root):
        delegated_node = (int(merkle_root, 16) % total_node) + 1
        return delegated_node

    # send to delegated_node
    # need to update
    def vote(delegated_node):

        return 0

    def generate_block(prev_hash, total_node, vote_result, tx_list=[]):
        transactions = tx_list
        merkle_cls = merkle.merkle_root()
        transactions = tx_list

        merkle_cls = merkle.MerkleTree()
        merkle_root = merkle_cls.get_merkle(transactions)
        vote_rate = (vote_result / total_node) * 100

        if vote_rate > 50:
            _difficulty = 10000

        elif vote_rate < 50:
            _difficulty = 100000

        else:
            _difficulty = 10000

        current_nonce = proof_of_work.proof_of_work(transactions, _difficulty)

        block_header = block.block_header()

        block_header.num_tx = len(tx_list)

        block_header_hash = hashlib.sha256(block_header).hexdigest()
        block_header.block_hash = block_header_hash

        block = Block.Block(block_header, tx_list)

        return block


'Test Code'
if __name__ == '__main__':

    'Test cal_candidate'
    merkle_root ="937ba9042411aae82e555f494619e745a061d3b095ef407367156b5ea6ab69cf"
    total_node = 10
    blind_vote=BlindVote
    delegated_node=blind_vote.cal_candidate(total_node,merkle_root)
    print(delegated_node)

    'Test cal_candidate'