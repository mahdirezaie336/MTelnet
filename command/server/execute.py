import os

from command import Command
from msocket import MSocket


class Execute(Command):

    def execute(self, socket: MSocket, args: list[str]) -> str:
        return os.popen(' '.join(args)).read()

    def help(self) -> str:
        return 'Executes a command into the connected node.\n'
