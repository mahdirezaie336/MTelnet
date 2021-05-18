import os

from command.command import Command


class Execute(Command):

    def execute(self, args) -> str:
        return os.popen(' '.join(args)).read()

    def help(self) -> str:
        return 'Executes a command into the connected node.\n\n'
