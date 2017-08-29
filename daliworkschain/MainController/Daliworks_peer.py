import http.client
import thread
import time
from TransactionManager import Daliworks_Transaction

from MainController import Property
from Network import Receiver
from StorageManager import FileController
from MainController import Set_Peer_num
from BlockManager import GenesisBlock_Generator
from BlockManager import BlockGenerator
from MerkleTree import GetMerkleHash

my_port = 10654


def main():

    FileController.remove_all_transactions()
    my_ip_address = FileController.get_my_ip()
    Property.my_ip_address = my_ip_address
    Set_Peer_num.Set_PeerNum()
    print "daliworks peer" + str(Property.my_peer_num)
    thread.start_new_thread(
        Receiver.start, ("Receiver", my_ip_address, my_port))
    GenesisBlock_Generator.generate_Genesisblock()

    while True:
        Daliworks_Transaction.Daliworks_Transaction()
        Merkle_hash = GetMerkleHash.GetMerkleHash()
        BlockGenerator.generate_block(Merkle_hash, my_port, my_ip_address)
        FileController.remove_all_transactions()
        time.sleep(60)

    thread.exit()


if __name__ == '__main__':
    main()
