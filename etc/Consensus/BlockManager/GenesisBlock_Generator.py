
def generate_Genesisblock():
    from BlockManager import Block
    from StorageManager import FileController
    import hashlib
    import json
    transactions = 'i am soo hwan'
    block_hash = hashlib.sha256(transactions).hexdigest()
    block_info = 'genesisblock'
    block_miner = 'soohwan'
    block_height = 1
    MerkleTree_Hash = hashlib.sha256(transactions).hexdigest()
    nonce = 0
    Difficulty =0
    previous_blockhash = 0





    block = Block.Block(block_hash,block_info,block_miner,block_height,MerkleTree_Hash,transactions,nonce,Difficulty,previous_blockhash)

    block_temp = json.dumps(block, indent=4, default=lambda o: o.__dict__, sort_keys=True)
    FileController.create_new_block(str(block_height), block_temp)

    print 'BlockCreate'