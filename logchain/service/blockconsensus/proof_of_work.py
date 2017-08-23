import hashlib
import time
import random
import math

MAX_NONCE = 2 ** 32

def proof_of_work(block_info, difficulty_bits):

    target = 2 ** (256-difficulty_bits)
    found = False
    start_time = time.time()

    i =1
    while (not found):

        nonce = random.randint(0,MAX_NONCE)
        hash_result = hashlib.sha256(str(block_info).encode('utf-8')+str(nonce).encode('utf-8')).hexdigest()

        # check if this is a valid result, below the target
        if int(hash_result, 16) <= target:

            print ("Success with nonce %d" % nonce, "log2=",math.log(nonce,2))
            print ("Hash is %s" % hash_result)
            found = True

            end_time = time.time()
            elapsed_time = end_time - start_time
            print ("Elapsed Time: %.4f seconds" % elapsed_time)

            if elapsed_time > 0:
                # estimate the hashes per second
                hash_power = float(int(i) / elapsed_time)
                print ("Try %d" %i)
                print ("Hashing Power: %ld hashes per second" % hash_power)
            return (hash_result,nonce,i)
        i=i+1

    print ("Failed after %d (max_nonce) tries" % nonce)
    return nonce

'Test Code'

if __name__ == '__main__':

    block_info = "73b5f3ea822853ad3a25fddcad685c3cf496b77ceb28200ff88a12564bc938684d4bfb60e8f6f09b4021d460df3749ebb588acf42f80b4fbdd862d6cdf0f9135"
    difficulty_bits = 11
    hash_result,nonce,i= proof_of_work(block_info,difficulty_bits)
    print (hash_result,nonce,i)