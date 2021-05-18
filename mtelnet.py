#!/usr/bin/env python3

from invoker import Invoker, CommandNotFoundException
import sys
from socket import SOCK_STREAM, AF_INET

from msocket import MSocket


class MTelnet:

    def __init__(self):
        self.socket = MSocket(AF_INET, SOCK_STREAM)
        self.command_factory = Invoker()

    def run(self, args):

        if len(args) > 1:
            pass

        try:
            while True:
                command = input('mtelnet> ').split()
                try:
                    r = self.command_factory.execute(command[0], command[1:])
                    print(r)
                except Exception as e:
                    print('error')
                    self.command_factory.help(command[0])

        except KeyboardInterrupt:
            print('\n\nProgram is terminating due to a keyboard interrupt.')
            self.socket.close()


t = MTelnet()
t.run(sys.argv)
