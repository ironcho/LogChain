import thread
import time


from TransactionManager import GenerateTransaction

from MainController import Property
from Network import Receiver
from StorageManager import FileController
from MainController import Set_Peer_num
from BlockManager import GenesisBlock_Generator
from BlockManager import BlockConfirm

my_port = 10654

def main():

    FileController.remove_all_transactions()
    my_ip_address = FileController.get_my_ip()
    Property.my_ip_address = my_ip_address
    Set_Peer_num.Set_PeerNum()
    print "my peer" + str(Property.my_peer_num)
    thread.start_new_thread(Receiver.start, ("Receiver", my_ip_address, my_port))
    GenesisBlock_Generator.generate_Genesisblock()

    while True:
        block_height, previous_blockhash, = FileController.get_last_block()
        if (block_height ==1):
            GenerateTransaction.GenerateTransaction()
        else:
            GenerateTransaction.GenerateTransaction()
        while True:
            time.sleep(60)
            break

    FileController.remove_all_transactions()

    thread.exit()
if __name__ == '__main__':
    main()