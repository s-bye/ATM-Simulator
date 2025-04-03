from datetime import datetime
from classes.transactions import Transaction
from classes.dao.baseDAO import BaseDAO
from classes.dao.userDAO import UserDAO


class TransactionDAO(BaseDAO):
    def __init__(self, db_file="bank_database.sqlite"):
        super().__init__(db_file)
        self.UserDao = UserDAO(db_file)

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

    def deposit(self, card_number, amount):
        conn = self.connect_db()
        cursor = conn.cursor()

        user = self.UserDao.get_user_by_card(card_number)
        if not user:
            conn.close()
            return "User not found"

        new_balance = user.get_balance() + amount
        cursor.execute("UPDATE users SET balance = ? WHERE card_number = ?", (new_balance, card_number))

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''INSERT INTO transactions (user_id, transaction_type, amount, timestamp)
                          VALUES (?, ?, ?, ?)''', (user.user_id, 'deposit', amount, timestamp))
        conn.commit()
        conn.close()
        return "Deposit successful"

    def withdraw(self, card_number, amount):
        conn = self.connect_db()
        cursor = conn.cursor()

        user = self.UserDao.get_user_by_card(card_number)
        if not user:
            conn.close()
            return "User not found"

        if user.get_balance() < amount:
            conn.close()
            return "Insufficient funds"

        new_balance = user.get_balance() - amount
        cursor.execute("UPDATE users SET balance = ? WHERE card_number = ?", (new_balance, card_number))

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''INSERT INTO transactions (user_id, transaction_type, amount, timestamp)
                            VALUES (?, ?, ?, ?)''', (user.user_id, 'withdraw', -amount, timestamp))

        conn.commit()
        conn.close()
        return "Withdrawal successful"

    def transfer_funds(self, sender_card, receiver_card, amount):
        conn = self.connect_db()
        cursor = conn.cursor()

        try:
            sender = self.UserDao.get_user_by_card(sender_card)
            receiver = self.UserDao.get_user_by_card(receiver_card)

            if not sender or not receiver:
                return "Invalid card number(s)"

            if sender.get_balance() < amount:
                return "Insufficient funds"

            new_sender_balance = sender.get_balance() - amount
            new_receiver_balance = receiver.get_balance() + amount

            cursor.execute("UPDATE users SET balance = ? WHERE card_number = ?", (new_sender_balance, sender_card))
            cursor.execute("UPDATE users SET balance = ? WHERE card_number = ?", (new_receiver_balance, receiver_card))

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute('''INSERT INTO transactions (user_id, transaction_type, amount, timestamp)
                              VALUES (?, ?, ?, ?)''', (sender.user_id, 'transfer', -amount, now))

            cursor.execute('''INSERT INTO transactions (user_id, transaction_type, amount, timestamp)
                                VALUES (?, ?, ?, ?)''', (receiver.user_id, 'transfer', amount, now))

            conn.commit()
            return "Transfer successful"
        except Exception as e:
            conn.rollback()
            return f"Transfer failed: {str(e)}"
        finally:
            conn.close()
