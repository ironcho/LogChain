import hashlib
import time
import random
import math

max_nonce = 2 ** 32 # 4 billion

def proof_of_work(block_info, difficulty_bits):


    # calculate the difficulty target
    target = 2 ** (256-difficulty_bits)

    print (hex(target))
    print (target)
    found = False
    start_time = time.time()
    i =1
    while (not found):
    	nonce = random.randint(0,max_nonce)
    #for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(block_info)+str(nonce)).hexdigest()

        # check if this is a valid result, below the target
        if long(hash_result, 16) <= target:
            print "Success with nonce %d" % nonce, "log2=",math.log(nonce,2)
            print "Hash is %s" % hash_result
	    found = True
            end_time = time.time()

            elapsed_time = end_time - start_time
            print "Elapsed Time: %.4f seconds" % elapsed_time
            if elapsed_time > 0:
                # estimate the hashes per second
                hash_power = float(long(i) / elapsed_time)
                print "Try %d" %i
                print "Hashing Power: %ld hashes per second" % hash_power
            return (hash_result,nonce,i)
        i=i+1

    print "Failed after %d (max_nonce) tries" % nonce
    return nonce




