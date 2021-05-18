from command.close import Close
from command.command import Command
from command.execute import Execute
from command.help import Help
from command.scan import Scan


class Invoker:

    _commands = dict[str: Command]

    def __init__(self):
        self._commands = {'close': Close(),
                          'help': Help(),
                          'exec': Execute(),
                          'scan': Scan()}

    def execute(self, name: str, args, socket) -> str:
        return self._commands[name].execute(socket, args)

    def help(self, name: str):
        return self._commands[name].help()


class CommandNotFoundException(Exception):

    def __init__(self, *args):
        super().__init__(*args)
