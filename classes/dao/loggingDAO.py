import sqlite3
from datetime import datetime
from baseDAO import BaseDAO


class LoggingDAO(BaseDAO):
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

        logs = [(log_id, user_id, action, timestamp) for log_id, user_id, action, timestamp in rows]
        return logs

    def get_all_logs(self):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM logs ORDER BY timestamp DESC""")
        rows = cursor.fetchall()
        conn.close()

        logs = [(log_id, user_id, action, timestamp) for log_id, user_id, action, timestamp in rows]
        return logs