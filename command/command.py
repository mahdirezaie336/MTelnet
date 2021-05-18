import abc


class Command:

    @abc.abstractmethod
    def execute(self, socket, args) -> str:
        pass

    @abc.abstractmethod
    def help(self) -> str:
        pass
