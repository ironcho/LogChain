from logchain.communication.p2p import Property
from logchain.communication.p2p import sender
from logchain.communication.p2p import receiver
from logchain.communication.p2p import node_mapping_table


class MainController(object):
    def __init__(self):
        return 0

    @staticmethod
    def command_line_interface():

        cmd = None

        while cmd != 'q':
            cmd = input('[t: send transaction, b: send block] > ')
            if cmd == 't':
                Sender.sending_tx()

            if cmd == 'b':
                Sender.sending_mining_block()


if __name__ == '__main__':
    node_mapping_table.initialize()
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", Property.my_node.self_node, Property.port)
    recv_thread.start()

    MainController.command_line_interface()


def test_p2p_mgr():
    node_mapping_table.initialize()
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", Property.my_node.self_node, Property.port)
    recv_thread.start()

    MainController.command_line_interface()
