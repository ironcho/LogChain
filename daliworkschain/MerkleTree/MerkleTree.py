from StorageManager import FileController
import hashlib
import time
import random
import math


def Get_Transaction():

    list=FileController.get_transaction_list()
    return list

def Transaction_Hash():
    list = Get_Transaction()
    Hash_list =[]
    i=0

    while i<len(list):
        hash_result = hashlib.sha256(str(list[i])).hexdigest()
        Hash_list.append(long(hash_result, 16))
        i=i+1

    i=0
    while i< len(Hash_list):
        Hash_list[i] = str(Hash_list[i])
        i=i+1

    return Hash_list


class MerkleTreeHash(object):
    def __init__(self):
        pass

    def find_merkle_hash(self,file_hashes):

        blocks = []

        if not file_hashes:
            raise ValueError("Missing required file hashed for computing merkle tree")

        blocks = file_hashes

        list_len = len(blocks)

        while list_len %2 != 0:
            blocks.extend(blocks[-1:])
            list_len = len(blocks)

        secondary =[]

        for k in [blocks[x:x+2] for x in xrange(0,len(blocks),2)]:
            hasher = hashlib.sha256()
            hasher.update(k[0]+k[1])
            secondary.append(hasher.hexdigest())


        if len(secondary) ==1:
            return secondary[0][0:64]
        else:
            #print str(self.find_merkle_hash(secondary))
            return self.find_merkle_hash(secondary)


#cls = MerkleTreeHash()
#MerkleTreeHash=cls.find_merkle_hash(Transaction_Hash())
