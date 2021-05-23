from command.command import Command
from msocket import MSocket


class Open(Command):

    def execute(self, socket: MSocket, args: list[str]) -> str:
        if len(args) < 2:
            raise ValueError('Not enough arguments to open connection.')
        if socket.is_connected():
            return 'Already connected.'


    def help(self) -> str:
        pass
