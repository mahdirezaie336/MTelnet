from command import Command
from msocket import MSocket


class Send(Command):

    def execute(self, socket: MSocket, args: list[str]) -> str:
        if len(args) < 1:
            raise ValueError('Not enough arguments to send message.')

        if '-e' in args:
            args.remove('-e')
            message = ' '.join(args).encode()
        else:
            message = ' '.join(args).encode()

        socket.send(message)
        response = socket.recv(1024)
        return response.decode()

    def help(self) -> str:
        return 'Sends a message to connected server.\n' \
               'Usage: send <message>\n' \
               '       send -e <message>\n'