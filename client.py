from socket import socket, AF_INET, SOCK_STREAM


class Client:

    def __init__(self, server_address: tuple[str, int]):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.server_address = server_address


