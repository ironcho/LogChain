import hashlib


class MerkleTree(object):
    def __init__(self):
        pass

    def get_merkle(self, p_items):
        """
        Get merkle tree root. It can be used for checking data integrity easily.
        Implemented using recursive alg.

        :param p_items: list of transactions -- list
        :return: Root of merkle tree -- string
        """

        blocks = []

        if not p_items:
            raise ValueError('')

        for m in sorted(p_items):
            blocks.append(m)

        list_len = len(blocks)

        # make even number of items in list
        while list_len % 2 != 0:
            blocks.extend(blocks[-1:])
            list_len = len(blocks)

        secondary = []

        for k in [blocks[x:x+2] for x in range(0, len(blocks), 2)]:
            hasher = hashlib.sha256()
            k[0] = k[0].encode('utf-8')
            k[1] = k[1].encode('utf-8')
            hasher.update(k[0] + k[1])
            secondary.append(hasher.hexdigest())

        if len(secondary) == 1:
            return secondary[0][0:64]

        # recursive
        else:
            return self.get_merkle(secondary)



