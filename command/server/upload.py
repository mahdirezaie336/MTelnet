from command import Command
from socket import socket as s
import os


class Upload(Command):

    PATH_TO_SAVE = './uploaded_files'

    def __init__(self):
        if not os.path.exists(Upload.PATH_TO_SAVE):
            os.makedirs(Upload.PATH_TO_SAVE)

    def execute(self, socket: s, args: list[str]) -> str:
        file_name = args.pop(0)
        file_bytes = ' '.join(args).encode()

        with open(os.path.join(Upload.PATH_TO_SAVE, file_name), 'wb') as file:
            file.write(file_bytes)

        return 'Saved successfully.'

    def help(self) -> str:
        return 'Saves sent file from client into a specific path.\n' \
               'Usage: upload file_name file_bytes\n'
