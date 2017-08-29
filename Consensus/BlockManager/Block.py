
class Block(object):
    type = 'B'
    block_hash =None
    block_miner = None
    block_height = None
    block_info = None
    Merkleroot_hash = None
    transactions = []
    time_stamp = None
    nonce = None
    Difficulty = None
    previous_blockhash = None


    def __init__(self,block_hash,block_info,block_miner,block_height,Merkleroot_hash,transactions,nonce,Difficulty,previous_blockhash):
        import time
        self.type = 'B'
        self.block_hash = block_hash
        self.block_info = block_info
        self.block_miner = block_miner
        self.block_height =block_height
        self.Merkleroot_hash = Merkleroot_hash
        self.transactions = transactions
        self.nonce =nonce
        self.Difficulty = Difficulty
        self.previous_blockhash = previous_blockhash
        self.time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime())

