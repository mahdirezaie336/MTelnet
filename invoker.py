from command.close import Close
from command.command import Command
from command.execute import Execute
from command.help import Help
from command.scan import Scan
from command.upload import Upload


class Invoker:

    _commands = dict[str: Command]

    def __init__(self):
        self._commands = {'close': Close(),
                          'help': Help(),
                          'exec': Execute(),
                          'scan': Scan(),
                          'upload': Upload()}

    def execute(self, name: str, args, socket) -> str:
        if name not in self._commands:
            raise CommandNotFoundException('Command not found.')
        return self._commands[name].execute(socket, args)

    def help(self, name: str):
        if name not in self._commands:
            raise CommandNotFoundException('Command not found.')
        return self._commands[name].help()


class CommandNotFoundException(Exception):

    def __init__(self, *args):
        super().__init__(*args)