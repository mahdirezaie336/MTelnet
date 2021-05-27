from command import Command
from msocket import MSocket
from shared_resources import SharedResources
from dbmanager import DBManager


class DBAdd(Command):

    def execute(self, socket: MSocket, args: list[str]) -> str:
        res = SharedResources()
        if 'db' not in res:
            db = DBManager()
            res.add_attribute('db', db)
        else:
            db = res.get_attribute('db')
        db.insert(' '.join(args))
        return 'Command added to database history'

    def help(self) -> str:
        pass
