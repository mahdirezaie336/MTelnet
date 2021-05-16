#!/usr/bin/env python3
from client import Client
import sys


def __main__():
    args = sys.argv
    c = Client((args[1], int(args[2])))
    c.start()


__main__()
