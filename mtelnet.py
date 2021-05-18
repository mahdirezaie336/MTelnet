#!/usr/bin/env python3
import os
import traceback

from Invoker import Invoker
from client import Client
from server import Server
from command import *
import sys
from socket import socket, SOCK_STREAM, AF_INET


class MTelnet:

    client_commands = ['upload', 'exec', 'send']
    server_commands = ['listen']
    other_commands = ['history', 'help']

    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.command_factory = Invoker()

    def run(self, args):

        if len(args) > 1:
            pass

        try:
            while True:
                command = input('mtelnet> ').split()
                if command[0] in MTelnet.client_commands or \
                        command[0] in MTelnet.server_commands or \
                        command[0] in MTelnet.other_commands:

                    try:
                        r = self.__getattribute__(command[0])(command[1:])
                        print(r)
                    except Exception as e:
                        print('error')
        except KeyboardInterrupt:
            traceback.print_exc('Program terminated by kill signal.')
            self.socket.close()

    def help(self, args) -> str:
        return '\nHello!\nThis is a program like telnet which is created by Mahdi Rezaie.\n' +\
              'Available commands are:\n\n' +\
              'help\t\t\t\t\t\t-\tPrints this message.\n'+\
              'upload <File Path>\t\t\t-\tUploads a file to server.\n'+\
              'exec <command>\t\t\t\t-\tExecutes a command inside the server\n'+\
              '\n'

    def exec(self, args):
        return os.system(' '.join(args))


t = MTelnet()
t.run(sys.argv)
