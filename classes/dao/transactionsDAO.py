from datetime import datetime
from classes.transactions import Transaction
from classes.dao.baseDAO import BaseDAO


class TransactionDAO(BaseDAO):
    def __init__(self, db_file="bank_database.sqlite"):
        super().__init__(db_file)

    def add_transaction(self, user_id, transaction_type, amount):
        conn = self.connect_db()
        cursor = conn.cursor()

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''INSERT INTO transactions (user_id, transaction_type, amount, timestamp)
                      VALUES (?, ?, ?, ?)''', (user_id, transaction_type, amount, timestamp))

        conn.commit()
        conn.close()

    def get_transactions_by_user_id(self, user_id):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM transactions WHERE user_id = ? ORDER BY timestamp DESC""", (user_id,))
        rows = cursor.fetchall()
        conn.close()

        transactions = [Transaction(*row) for row in rows]
        return transactions

    def get_all_transactions(self):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM transactions ORDER BY timestamp DESC""")
        transactions = cursor.fetchall()
        conn.close()
        return transactions

