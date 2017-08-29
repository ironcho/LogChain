import thread
from MainController import Property
from Network import Receiver
from StorageManager import FileController
from BlockManager import GenesisBlock_Generator
from MainController import Set_Peer_num
my_port = 10654

def main():

    my_ip_address = FileController.get_my_ip()
    Property.my_ip_address = my_ip_address
    Set_Peer_num.Set_PeerNum()
    print "my peer"+str(Property.my_peer_num)
    FileController.remove_all_transactions()

    thread.start_new_thread(Receiver.start, ("Receiver", my_ip_address, my_port))
    GenesisBlock_Generator.generate_Genesisblock()

    print "RECEIVER START"

    while True:
            FileController.remove_all_transactions()

if __name__ == '__main__':
    main()