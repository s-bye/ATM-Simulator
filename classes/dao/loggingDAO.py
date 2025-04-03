import sqlite3
from datetime import datetime
from classes.dao.baseDAO import BaseDAO
from classes.logging import Logging


class LoggingDAO(BaseDAO):
    def __init__(self, db_file="bank_database.sqlite"):
        super().__init__(db_file)

    def add_log(self, user_id, action):
        conn = self.connect_db()
        cursor = conn.cursor()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""INSERT INTO logs (user_id, action, timestamp)
        VALUES (?, ?, ?)""", (user_id, action, timestamp))

        conn.commit()
        conn.close()

    def get_logs_by_user_id(self, user_id):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM logs WHERE user_id = ? ORDER BY timestamp DESC""", (user_id,))
        rows = cursor.fetchall()
        conn.close()

        logs = [Logging(*row) for row in rows]
        return logs

    def get_all_logs(self):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM logs ORDER BY timestamp DESC""")
        rows = cursor.fetchall()
        conn.close()

        logs = [Logging(*row) for row in rows]
        return logs

    def delete_logs_by_user_id(self, id):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute(''' DELETE FROM logs WHERE user_id = ? ''', (id,))
        conn.commit()
        conn.close()

    def delete_all_logs(self):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute(''' DELETE FROM logs''')
        cursor.execute(''' DELETE FROM sqlite_sequence WHERE name = 'logs' ''')
        conn.commit()
        conn.close()
