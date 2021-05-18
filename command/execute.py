import os

from command.command import Command


class Execute(Command):

    def execute(self, args) -> str:
        return os.popen(' '.join(args)).read()
