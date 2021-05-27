import socket
from socket import socket as s
import ssl


class MSocket:

    def __init__(self):
        self.__client_socket = s()
        self.__server_socket = s()
        self.__listening = False
        self.__connected = False
        self.__context = ssl.create_default_context()
        self.__secured_socket = None
        self.__secured_connected = False

    def send(self, data: bytes, secured=False):
        if not self.__connected:
            raise ConnectionError('No connection.')
        if not secured:
            self.__client_socket.send(data)
        else:
            hostname = self.__client_socket.getpeername()[0]
            if not self.__secured_connected:
                self.__secured_socket = self.__context.wrap_socket(self.__client_socket, server_hostname=hostname)
            self.__secured_socket.send(data)

    def connect(self, address: tuple[str, int]):
        r = self.__client_socket.connect(address)
        self.__connected = True
        return r

    def listen(self, address_to_bind: tuple[str, int]):
        self.__server_socket.bind(address_to_bind)
        self.__server_socket.listen()
        self.__listening = True

    def accept(self):
        return self.__server_socket.accept()

    def is_listening(self):
        return self.__listening

    def is_connected(self) -> bool:
        return self.__connected

    def close(self):
        self.__listening = False
        self.__connected = False
        self.__client_socket.close()
        self.__server_socket.close()

    def recv(self, size=1024):
        return self.__client_socket.recv(size)

    def recv_all(self):
        data = b''
        while (d := self.__client_socket.recv(1024)) != b'':
            data += d
        return data
