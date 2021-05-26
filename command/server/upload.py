from command import Command
from msocket import MSocket


class Upload(Command):

    def execute(self, socket: MSocket, args: list[str]) -> str:
        pass

    def help(self) -> str:
        pass
