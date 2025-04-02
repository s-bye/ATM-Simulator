import sqlite3


class BaseDAO:
    def __init__(self, db_file="bank_database.sqlite"):
        self.db_file = db_file

    def connect_db(self):
        return sqlite3.connect(self.db_file)

