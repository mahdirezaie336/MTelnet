#!/usr/bin/env python3

from invoker import Invoker, CommandNotFoundException
from command import *
from command.execute import Execute
import sys

from msocket import MSocket


class MTelnet:

    def __init__(self):
        self.socket = MSocket()
        self.command_factory = Invoker({'close': Close(),
                                        'help': Help(),
                                        'exec': Execute(),
                                        'scan': Scan(),
                                        'upload': Upload(),
                                        'open': Open(),
                                        'listen': Listen(),
                                        'send': Send(),
                                        'dbadd': DBAdd(),
                                        'history': History()
                                        })

    def run(self, args):

        if len(args) > 1:
            pass

        try:
            while True:
                input_command = input('mtelnet> ').split(' ')
                if len(input_command) == 0:
                    continue
                try:
                    r = self.command_factory.execute(input_command[0], input_command[1:], self.socket)
                    print(r)
                except CommandNotFoundException:
                    print('Command not found. Type help to see available commands.')
                except KeyboardInterrupt as e:
                    raise e
                except Exception as e:
                    print('Command <{}> usage error: {}\nHelp:'.format(input_command[0], str(e)))
                    print(self.command_factory.help(input_command[0]))
                finally:
                    self.command_factory.execute('dbadd', input_command, None)

        except KeyboardInterrupt:
            print('\n\nProgram is terminating due to a keyboard interrupt.')
            self.socket.close()


t = MTelnet()
t.run(sys.argv)
