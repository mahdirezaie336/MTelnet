from command.command import Command
from msocket import MSocket


class Upload(Command):

    def help(self) -> str:
        return 'Usage: upload <path>\n\nSends file specified with <path> through the socket.'

    def execute(self, socket: MSocket, args) -> str:
        if not socket.is_connected():                               # If socket is not connected
            raise ConnectionError('No Connection.')

        with open(args[0], 'rb') as file:                           # Sending file over socket
            while (buff := file.read(1024)) != b'':
                socket.send(buff)
            socket.send(b' ')

        return 'done.'
