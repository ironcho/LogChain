

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


if __name__ == '__main__':
    block_h_test = BlockHeader('t','t','t','t')
    transactions = [
        '{"recv_addr": "1", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"recv_addr": "2", "tx_id": "T20170118095955", "time_stamp": "20170118095955", "pub_key": "", "type": "T", "message": "1073382bc80d8cc2828f790b4ff148ae1ef145260000ebb884a15bf9"}',
        '{"recv_addr": "3", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"recv_addr": "4", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"recv_addr": "5", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"recv_addr": "6", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"recv_addr": "7", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"recv_addr": "8", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26cf9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"recv_addr": "9", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T20170118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T201270118092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}',
        '{"rec_addr": "10", "tx_id": "T2017018092904", "time_stamp": "20170118092904", "pub_key": "", "type": "T", "message": "da7f6e26c3f9183399be2adb5d8ec6b9b2c211a0955a6ec8a24bc66f"}'
    ]
    print(block_h_test)

    block_test = Block(block_h_test,transactions )
    print(block_test.block_header)