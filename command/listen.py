from command.command import Command
from msocket import MSocket
from threading import Thread
from shared_resources import SharedResources
from invoker import Invoker
from socket import socket as s

from command.server import *


class Listen(Command):
    __invoker = Invoker({'exec': Execute(),
                         'help': ''})

    def client_handler(self, socket: s):
        while True:
            command = socket.recv(1024).decode().split()
            print('{}: Running command'.format(socket.getpeername()), command[0])
            r = self.__invoker.execute(command[0], command[1:], socket)
            socket.send(r.encode())

    def welcome(self, socket: MSocket):
        while True:
            print('Welcoming Socket: Waiting for clients ...')
            client_socket, address = socket.accept()
            print('Welcoming Socket: Client', address, 'accepted.')
            t = Thread(name=address, target=self.client_handler, args=(client_socket,))
            t.start()
            SharedResources().get_attribute('server_threads').append(t)

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
        Thread(name='welcome', target=self.welcome, args=(socket,)).start()
        return 'Socket is listening on port {}'.format(args[1])

    def help(self) -> str:
        return 'Listens on a port for clients to connect.\n\n' \
               'Usage: listen <port number>'
