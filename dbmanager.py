import mysql.connector


class DBManager:

    def __init__(self, db_name='mtelnet', db_table='history'):
        self.__db_name = db_name
        self.__db_table = db_table
        self.__db = mysql.connector.connect(host='localhost', user='mahdi', password='1q2w3e4R')
        self.__cr = self.__db.cursor()
        cr = self.__cr
        cr.execute('create database if not exists {}'.format(db_name))
        cr.execute('use {}'.format(db_name))
        cr.execute('create table if not exists {} (command char(255))'.format(db_table))

    def insert(self, string: str):
        self.__cr.execute('insert into {} (command) values ("{}")'.format(self.__db_table, string))
        self.__db.commit()

    def read_all(self) -> str:
        self.__cr.execute('select * from {}'.format(self.__db_table))
        data = self.__cr.fetchall()
        data_list = []
        for item in data:
            data_list.append(item[0])
        return '\n'.join(data_list)
