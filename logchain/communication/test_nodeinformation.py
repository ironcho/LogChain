import socket

def get_ip():
    return socket.gethostbyname_ex(socket.gethostname())



my_ip = get_ip()


print(my_ip)
