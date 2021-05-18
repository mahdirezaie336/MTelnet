import abc

from msocket import MSocket


class Command:

    @abc.abstractmethod
    def execute(self, socket: MSocket, args: list[str]) -> str:
        pass

    @abc.abstractmethod
    def help(self) -> str:
        pass
