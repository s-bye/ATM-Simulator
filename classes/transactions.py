import sqlite3

class Transaction:
    def __init__(self, transaction_id, user_id, transaction_type, amount, timestamp):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.transaction_type = transaction_type
        self._amount = amount
        self.timestamp = timestamp

    def __repr__(self):
        return f"Transaction(transaction_id={self.transaction_id}, user_id={self.user_id}, " \
               f"transaction_type={self.transaction_type}, amount={self.amount}, timestamp={self.timestamp})"

class TransactionDAO:
    def __init__(self, db_file="bank_database.sqlite"):
        self.db_file = db_file

    def _connect(self):
        return sqlite3.connect(self.db_file)

    def add_transaction(self, transaction):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM transactions WHERE user_id = ? ORDER BY timestamp DESC""", (transaction.user_id,))
        rows = cursor.fetchall()

        transactions = [Transaction(*row) for row in rows]
        return transactions

    def get_transactions_by_user_id(self, user_id):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM transactions WHERE user_id = ? ORDER BY timestamp DESC""", (user_id,))
        rows = cursor.fetchall()
        conn.close()

        transactions = [Transaction(*row) for row in rows]
        return transactions

    def get_all_transactions(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM transactions ORDER BY timestamp DESC""")
        rows = cursor.fetchall()
        conn.close()

        transactions = [Transaction(*row) for row in rows]
        return transactions

