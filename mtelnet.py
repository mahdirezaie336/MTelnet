#!/usr/bin/env python3

from invoker import Invoker, CommandNotFoundException
import sys

from msocket import MSocket


class MTelnet:

    def __init__(self):
        self.socket = MSocket()
        self.command_factory = Invoker()

    def run(self, args):

        if len(args) > 1:
            pass

        try:
            while True:
                command = input('mtelnet> ').split()
                try:
                    r = self.command_factory.execute(command[0], command[1:], self.socket)
                    print(r)
                except CommandNotFoundException:
                    print('Command not found. Type help to see available commands.')
                except:
                    print('Command usage error.\n')
                    print(self.command_factory.help(command[0]))

        except KeyboardInterrupt:
            print('\n\nProgram is terminating due to a keyboard interrupt.')
            self.socket.close()


t = MTelnet()
t.run(sys.argv)
