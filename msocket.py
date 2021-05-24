import socket
from socket import socket as s


class MSocket:

    def __init__(self):
        self.__client_socket = s()
        self.__server_socket = s()
        self.__listening = False
        self.__connected = False

    def send(self, data: bytes):
        self.__client_socket.send(data)

    def connect(self, address: tuple[str, int]):
        return self.__client_socket.connect(address)

    def listen(self, address_to_bind: tuple[str, int]):
        self.__server_socket.bind(address_to_bind)
        return self.__server_socket.listen()

    def accept(self):
        return self.__server_socket.accept()

    def is_listening(self):
        return self.__listening

    def is_connected(self) -> bool:
        return self.__connected

    def close(self):
        self.__client_socket.close()
        self.__server_socket.close()
