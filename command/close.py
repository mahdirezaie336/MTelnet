import sys

from command.command import Command


class Close(Command):

    def execute(self, socket, args) -> str:
        sys.exit(0)

    def help(self) -> str:
        return 'Closes the mtelnet program.\n'
