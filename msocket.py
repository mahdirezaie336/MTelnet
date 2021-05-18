import socket
from socket import socket as s


class MSocket(s):

    def __init__(self, *args):
        super().__init__(*args)
        self._address = None

    def is_connected(self) -> bool:
        try:
            self.getpeername()
        except OSError as e:
            if e.errno == 107:
                return False
            raise e
        return True
