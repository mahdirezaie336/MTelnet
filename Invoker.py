from command.Close import Close
from command.command import Command
from command.execute import Execute
from command.help import Help


class Invoker:

    _commands = dict[str: Command]

    def __init__(self):
        self._commands = {'close': Close(),
                          'help': Help(),
                          'exec': Execute()}

    def execute(self, name: str, args) -> str:
        return self._commands[name].execute(args)
