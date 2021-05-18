import abc


class Command:

    @abc.abstractmethod
    def execute(self, args) -> str:
        pass
