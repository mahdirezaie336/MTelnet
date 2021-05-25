# from command.command import Command


class Invoker:

    _commands = dict[str]

    def __init__(self, commands):
        self._commands = commands

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
