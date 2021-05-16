from socket import socket, AF_INET, SOCK_STREAM


class Client:

    def __init__(self, server_address: tuple[str, int]):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.server_address = server_address

    def start(self, message=None) -> str:
        message: str
        self.socket.connect(self.server_address)

        print('Connected to', self.server_address[0] + ':', self.server_address[1], '\n')
        print(self.socket.recv(4096).decode())

        if message is not None:
            self.socket.sendto(message.encode(), self.server_address)
            print(self.socket.recv(4096).decode())
        while True:
            message = input()
            self.socket.sendto(message.encode(), self.server_address)
            print(self.socket.recv(4096).decode())
