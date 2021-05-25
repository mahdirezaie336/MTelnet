from command.command import Command
from msocket import MSocket
from threading import Thread
from shared_resources import SharedResources


class Listen(Command):

    def client_handler(self, socket):
        pass

    def welcome(self, socket: MSocket):
        while True:
            s, address = socket.accept()
            t = Thread(name=address, target=self.client_handler, args=(s,))
            SharedResources()

    def execute(self, socket: MSocket, args: list[str]) -> str:
        if len(args) < 1:
            raise ValueError('Not enough arguments to listen.')
        if socket.is_listening():
            return 'Socket is already listening.'
        if len(args) == 1:
            address = ('0.0.0.0', int(args[0]))
        else:
            address = (args[0], int(args[1]))
        socket.listen(address)
        SharedResources().add_attribute('server_threads', [])
        return 'Socket is listening on port {}'.format(args[1])

    def help(self) -> str:
        pass
