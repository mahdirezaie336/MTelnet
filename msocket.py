import socket
from socket import socket as s


class MSocket(s):

    def __init__(self, *args):
        super().__init__(*args)

    def is_closed(self) -> bool:
        try:
            data = self.recv(16, socket.MSG_DONTWAIT | socket.MSG_PEEK)
            if len(data) == 0:
                return True
        except BlockingIOError:
            return False  # socket is open and reading from it would block
        except ConnectionResetError:
            return True  # socket was closed for some other reason
        except Exception as e:
            return False
        return False
