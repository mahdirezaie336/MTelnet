from command.Close import Close
from command.command import Command
from command.help import Help


class Invoker:

    _commands = dict[str: Command]

    def __init__(self):
        self._commands = {'close': Close(),
                          'help': Help()}

    def execute(self, name: str, args) -> str:
        return self._commands[name].execute(args)
