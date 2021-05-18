import sys

from command.command import Command


class Close(Command):

    def execute(self, args) -> str:
        sys.exit(0)

    def help(self) -> str:
        return 'Closes the mtelnet program.\n\n'
