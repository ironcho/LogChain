def voting(Merkle_hash):
    vote_number = (long(Merkle_hash,16) % 5)+1
    return vote_number