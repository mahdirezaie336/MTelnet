#!/usr/bin/env python3
import traceback

from Invoker import Invoker
import sys
from socket import socket, SOCK_STREAM, AF_INET


class MTelnet:

    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
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

        except KeyboardInterrupt:
            print('\n\nProgram is terminating due to a keyboard interrupt.')
            self.socket.close()


t = MTelnet()
t.run(sys.argv)
