import socket
from socket import socket as s


class MSocket:

    def __init__(self):
        self.client_socket = s()
        self.server_socket = s()

    def is_listening(self):
        return self.server_socket.getsockname() != ('0.0.0.0', 0)

    def is_connected(self) -> bool:
        try:
            self.client_socket.getpeername()
        except OSError as e:
            if e.errno == 107:
                return False
            raise e
        return True

    def close(self):
        self.client_socket.close()
        self.server_socket.close()
