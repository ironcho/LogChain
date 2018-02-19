import threading
import queue

from socket import *

data_queue = queue.Queue()

class Server(threading.Thread):
    def __init__(self, parent=None):
        threading.Thread.__init__(self)

    def run(self):
        sock = socket(AF_INET, SOCK_STREAM)
        addr = ('127.0.0.1', 1984)
        sock.bind(addr)
        sock.listen(5)
        print('SERVER READY')
        while True:
            request_sock, request_ip = sock.accept()
            recv_data = []
            while True:
                data = request_sock.recv(1024)
                if not data:
                    break
                recv_data.append(data)

            temp = ""
            for i in recv_data:
                temp += i.decode('utf-8')
            print(self.split_data(temp))

    def split_data(self, msg):
        msg = msg.split('.')

        header = msg[0]
        count = msg[1]
        body = []

        for index in range(0, int(count)):
            body.append(msg[2+index])

        if header == 'log':
            return '[DEBUG] LOG DATA : ' + body[0]
        elif header == 'block':
            pass
        elif header == 'transaction':
            pass
        elif header == 'status':
            pass
