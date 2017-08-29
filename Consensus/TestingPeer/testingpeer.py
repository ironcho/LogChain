import thread
import time
from MerkleTree import GetMerkleHash
from MainController import Property
from Network import Receiver
from StorageManager import FileController
from ConsensusManager import Voting
from ConsensusManager import SendVote
from ConsensusManager import Result_Voting
from BlockManager import GenesisBlock_Generator
from BlockManager import BlockGenerator
from MainController import Set_Peer_num
from BlockManager import BlockConfirm
my_port = 10654

def main():

    my_ip_address = FileController.get_my_ip()
    Property.my_ip_address = my_ip_address
    Set_Peer_num.Set_PeerNum()
    print "my peer"+str(Property.my_peer_num)
    FileController.remove_all_transactions()
    FileController.remove_all_voting()

    thread.start_new_thread(Receiver.start, ("Receiver", my_ip_address, my_port))
    GenesisBlock_Generator.generate_Genesisblock()

    print "RECEIVER START"

    while True:

        list=FileController.get_transaction_list()
        Count_Transaction=len(list)


        if Count_Transaction ==10:
            block_height, previous_blockhash, = FileController.get_last_block()
            Merkle_hash=GetMerkleHash.GetMerkleHash()
            vote_number=Voting.voting(Merkle_hash)
            SendVote.Send_Vote(vote_number)

            time.sleep(10)

            Difficulty = Result_Voting.result_voting()

            if Difficulty:
                print 'Block create'
                BlockGenerator.generate_block(Merkle_hash,Difficulty,my_port,my_ip_address)


            BlockCreating= False

            while not(BlockCreating):
                time.sleep(1)
                current_block_height, previous_blockhash, = FileController.get_last_block()
                if current_block_height>block_height:
                    BlockCreating = True
                    print'resetup'
                    break

            FileController.remove_all_transactions()
            FileController.remove_all_voting()


if __name__ == '__main__':
    main()