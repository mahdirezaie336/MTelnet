from command.command import Command
from msocket import MSocket


class Chat(Command):

    def receiver(self, socket):
        pass

    def sender(self, socket):
        pass

    def execute(self, socket: MSocket, args: list[str]) -> str:
        pass

    def help(self) -> str:
        pass
