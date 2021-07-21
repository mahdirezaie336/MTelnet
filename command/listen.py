from command.command import Command
from msocket import MSocket
from threading import Thread
from shared_resources import SharedResources
from invoker import Invoker, CommandNotFoundException
from socket import socket as s
import sys

from command.server import *


class Listen(Command):
    __invoker = Invoker({'exec': Execute(),
                         'help': Help(),
                         'upload': Upload()})

    @staticmethod
    def read_all(socket: s) -> bytes:
        all_bytes = socket.recv(1024*1024*50)
        return all_bytes

    def client_handler(self, socket: s):
        global data
        while True:
            try:
                data = Listen.read_all(socket).decode()
                command = data.split(' ')
                # print(command)
                if len(command) > 0 and command[0] == 'quit':
                    break
                if not command:
                    continue
                # Running Command
                r = self.__invoker.execute(command[0], command[1:], socket)
                if r == '':
                    r = ' '
                socket.send(r.encode())
            except CommandNotFoundException as e:
                print('Server received message:', data, file=sys.stderr)
                socket.send('Done'.encode())
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)
                break

    def welcome(self, socket: MSocket):
        while True:
            print('Welcoming Socket: Waiting for clients ...\n', file=sys.stderr)
            client_socket, address = socket.accept()
            print('Welcoming Socket: Client', address, 'accepted.', file=sys.stderr)
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
        return 'Socket is listening on port {}'.format(address[1])

    def help(self) -> str:
        return 'Listens on a port for clients to connect.\n\n' \
               'Usage: listen <port number>\n'
