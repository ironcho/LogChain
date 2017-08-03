import socket

def Main():
    #udp는 매번 누구로 부터 데이터가 누구로 부터 가는지 그때 마다 하는것.
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started.")

    while True:
        data, addr = s.recvfrom(1024)
        print("message from: " + str(addr))
        print("from connect user: " + str(data))
        data = str(data).upper()
        print("sending: " + str(data))
        byte_message = data.encode()
        s.sendto(byte_message, addr)
    s.close()

if __name__ == '__main__':
    Main()
