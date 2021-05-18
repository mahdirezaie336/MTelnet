from socket import socket, AF_INET, SOCK_STREAM
import threading


class Server:

    def __init__(self, port=16800):
        self.port = port
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(('0.0.0.0', port))

    def start(self):

        def client_handler(sock: socket):
            while True:
                data = sock.recv(4096)
                sock.sendall(data)

        print('Listening on port', self.port, '...')
        self.socket.listen()

        i = 0
        while True:
            print('Waiting for clients ...')
            client_socket, address = self.socket.accept()
            threading.Thread(name=str(i), target=client_handler, args=(client_socket,)).start()
            i += 1

