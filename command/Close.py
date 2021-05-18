import sys

from command.command import Command


class Close(Command):

    def execute(self, args) -> str:
        sys.exit(0)
