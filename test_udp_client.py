import socket

def Main():
    #udp는 매번 누구로 부터 데이터가 누구로 부터 가는지 그때 마다 하는것.
    host = '127.0.1.1'

    port = 5000

    server = ('127.0.0.1', 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("-> ")
    while message != 'q':
        fmessage = message.encode()
        s.sendto(fmessage, server)
        data, addr = s.recvfrom(1024)
        print ('Recieved from server: ' + str(data))
        message = input("-> ")

    s.close()

if __name__ == '__main__':
    Main()