from command import Command
from msocket import MSocket


class Send(Command):

    def execute(self, socket: MSocket, args: list[str]) -> str:
        if len(args) < 1:
            raise ValueError('Not enough arguments to send message.')

        if args[0] == '-e':
            message = args[1].encode()
        else:
            message = args[0].encode()

        socket.send(message)
        response = socket.recv(1024)
        return response.decode()

    def help(self) -> str:
        return 'Sends a message to connected server.\n' \
               'Usage: send <message>\n' \
               '       send -e <message>\n'
