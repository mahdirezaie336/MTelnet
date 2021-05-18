from command.command import Command


class Help(Command):

    def execute(self, args) -> str:
        return '\nHello!\nThis is a program like telnet which is created by Mahdi Rezaie.\n' + \
               'Available commands are:\n\n' + \
               'help\t\t\t\t\t\t-\tPrints this message.\n' + \
               'upload <File Path>\t\t\t-\tUploads a file to server.\n' + \
               'exec <command>\t\t\t\t-\tExecutes a command inside the server\n' + \
               '\n'
