from logging import log

if __name__ == '__main__':
    server = log.Server()
    server.start()
    server.join()