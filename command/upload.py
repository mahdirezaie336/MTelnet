from command.command import Command
from msocket import MSocket
import os


class Upload(Command):

    def help(self) -> str:
        return 'Usage: upload <path>\n\nSends file specified with <path> through the socket.'

    def execute(self, socket: MSocket, args) -> str:
        if not socket.is_connected():                               # If socket is not connected
            raise ConnectionError('No Connection.')

        file_address = args[0]
        file_name = os.path.basename(file_address)
        bytes_to_send = 'upload {} '.format(file_name).encode()
        with open(file_address, 'rb') as file:                           # Sending file over socket
            while (buff := file.read(1024)) != b'':
                bytes_to_send += buff

        socket.send(bytes_to_send)
        return 'done.'
