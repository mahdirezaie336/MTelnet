from command import Command
from msocket import MSocket
from shared_resources import SharedResources
from dbmanager import DBManager


class History(Command):

    def execute(self, socket: MSocket, args: list[str]) -> str:
        result = ''
        res = SharedResources()
        if 'db' not in res:
            db = DBManager()
            res.add_attribute('db', db)
        else:
            db = res.get_attribute('db')
        result += db.read_all()
        return result

    def help(self) -> str:
        return 'Prints a history of all command which you have input.\n'
