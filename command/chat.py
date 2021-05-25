from command.command import Command
from msocket import MSocket


class Chat(Command):

    def receiver(self, socket: MSocket):
        print('Waiting for client ...')
        s = socket.accept()
        while True:
            pass

    def sender(self, socket: MSocket):
        pass

    def execute(self, socket: MSocket, args: list[str]) -> str:
        pass

    def help(self) -> str:
        pass
