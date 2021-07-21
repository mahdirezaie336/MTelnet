from command import Command
from msocket import MSocket


class Help(Command):

    def execute(self, socket: MSocket, args: list[str]) -> str:
        return 'This is help message of server'

    def help(self) -> str:
        return self.execute(None, None)
