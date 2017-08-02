

class BlockHeader():

    def __init__(self, prev_hash, nonce, merkle_root, vote_result, timestamp=0):
        """

        :param prev_hash:
        :param nonce:
        :param merkle_root:
        :param vote_result:
        :param timestamp:
        """
        self.block = None
        self.block_id = None
        self.block_number = None
        self.vote_result = None
        self.block_hash = None
        self.num_tx = None

        self.nonce = nonce
        self.prev_hash = prev_hash
        self.merkle_root = merkle_root
        self.timestamp = timestamp


class Block():

    def __init__(self, block_header, tx_list=[]):
        """

        :param block_header:
        :param tx_list:
        """
        self.block_header = block_header
        self.tx_list = tx_list

