import Property
import Sender
import Receiver
import NodeMappingTable


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

    NodeMappingTable.set_node()
    NodeMappingTable.initialize()
    recv_thread = Receiver.ReceiverThread(1, "RECEIVER", Property.my_node.self_node, Property.port)
    recv_thread.start()

    MainController.command_line_interface()