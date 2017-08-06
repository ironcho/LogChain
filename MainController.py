import socket

import Property
import Sender
import Receiver
import json

class MainController(object):
    def __init__(self):
        return 0

    @staticmethod
    def set_node():

        Property.my_ip = socket.gethostbyname(socket.gethostname())
        return True

    @staticmethod

    def command_line_interface():

        cmd = None

        while cmd != 'q':
            cmd = input('[t: send transaction, b: send block] > ')
            #추후에 노드 관리를 하는 부분을 이용하여 매인 시나리오를 잘 돌릴수 있도록..nodeinfo.txt를 생성.
            if cmd == 't':
                #receiver, message가 결국 내용이다. '내가 누구에게 무슨 내용을 보낸다.' 라는 내용의 트랜잭션
                #receiver = raw_input('Receiver IP: ')
                #message = raw_input('Message: ')
                #이미 만들어진 트랜잭션을 이용하여 전송. new_transaction.txt.로 저장이 되어있다면.
                #trx_jstr = TransactionCotroller.create_transaction(Property.pub_key, Property.pri_key, receiver, message)

                #new_transaction.txt open
                f = open("transaction_new0.txt", 'r')
                transaction = f.read()
                transactions = json.loads(transaction)

                Sender.send_to_all(transaction)
                #print trx_jstr
                #Sender.send_to_all(trx_jstr)
                Property.tx_count += 1
                f.close()
            if cmd == 'b':
                f = open("block0.txt", 'r')
                block = f.read()

                Sender.send_to_all(block)

           # elif cmd =='s': #이 커맨드가 새로 네트워크에 참여할때의 커맨드
           #  Sender.send('192.168.99.1','tttt',10654)


if __name__ == '__main__':
    MainController.set_node()
    print (Property.my_ip)
    recv_thread = Receiver.ReceiverThread(1, "RECEIVER", Property.my_ip, Property.port)
    recv_thread.start()

    MainController.command_line_interface()