from command.Close import Close
from command.command import Command


class Invoker:

    _commands = dict[str: Command]

    def __init__(self):
        self._commands = {'close': Close(),
                          'help': None}

    def add_command(self, name: str, command: Command):
        self._commands[str] = command

    def execute(self, name: str, args) -> str:
        return self._commands[name].execute(args)
