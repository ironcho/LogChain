import MerkleTree

def GetMerkleHash():
    cls = MerkleTree.MerkleTreeHash()
    MerkleTreeHash = cls.find_merkle_hash(MerkleTree.Transaction_Hash())
    return MerkleTreeHash

#testcode
#merkletreehash = GetMerkleHash()
#print merkletreehash