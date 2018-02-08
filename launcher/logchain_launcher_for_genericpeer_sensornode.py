import logging
import sys
from PyQt5 import QtWidgets
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication.p2p import receiver
from service.blockmanager import genesisblock
from communication.msg_dispatch import dispatch_queue_list
from communication.msg_dispatch import t_type_queue_thread
from communication.msg_dispatch import b_type_queue_thread
from communication.msg_dispatch import v_type_queue_thread
from communication.peermgr import peerconnector
from monitoring import monitoring
from supplychain.supplychain_ui import main_ui



# Logchain launcher function for GenericPeer
# GenericPeer performs the role of PeerConnector in parallel.
def initialize_process_for_generic_peer():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # UI form to show the execution log of logchain
    monitoring.Main_form = monitoring.Form()

    logging.info("Start Logchain launcher for TrustPeer...")
    monitoring.Main_form.add_queue_data("log.Start Logchain launcher for GenericPeer...")

    initialize()

    # node add test
    monitoring.Main_form.add_node('test_node', '192.168.0.1', 'node.png')

    logging.info('Run processes for PeerConnector.')
    monitoring.Main_form.add_queue_data("log.Run processes for PeerConnector.")

    if not peerconnector.start_peerconnector():
        logging.info('Aborted because PeerConnector execution failed.')
        return


    set_peer.set_my_peer_num()
    logging.info("My peer num: " + str(nodeproperty.My_peer_num))

    'Genesis Block Create'
    genesisblock.genesisblock_generate()

    logging.info("Start a thread to receive messages from other peers.")
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.My_IP_address, nodeproperty.My_receiver_port)
    recv_thread.start()
    logging.info("The thread for receiving messages from other peers has started.")


    t_type_qt = t_type_queue_thread.TransactionTypeQueueThread(
        1, "TransactionTypeQueueThread",
        dispatch_queue_list.T_type_q,
        dispatch_queue_list.Connected_socket_q
    )
    t_type_qt.start()

    v_type_qt = v_type_queue_thread.VotingTypeQueueThread(
        1, "VotingTypeQueueThread",
        dispatch_queue_list.V_type_q,
        dispatch_queue_list.Connected_socket_q
    )
    v_type_qt.start()

    b_type_qt = b_type_queue_thread.BlockTypeQueueThread(
        1, "BlockTypeQueueThread",
        dispatch_queue_list.B_type_q,
        dispatch_queue_list.Connected_socket_q
    )
    b_type_qt.start()


def initialize():
    logging.info('Start the blockchain initialization process...')
    file_controller.remove_all_transactions()
    file_controller.remove_all_blocks()
    file_controller.remove_all_voting()
    logging.info('Complete the blockchain initialization process...')
    set_peer.init_myIP()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = main_ui.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    initialize_process_for_generic_peer()

    sys.exit(app.exec_())




