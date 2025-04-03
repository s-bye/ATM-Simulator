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

        current_balance = self.UserDao.get_balance(card_number)
        print(f"[DEBUG] Текущий баланс перед депозитом: {current_balance}")
        new_balance = current_balance + amount
        print(f"[DEBUG] Новый баланс после депозита: {new_balance}")
        cursor.execute("UPDATE users SET balance = ? WHERE card_number = ?", (new_balance, card_number))

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''INSERT INTO transactions (user_id, transaction_type, amount, timestamp)
                          VALUES (?, ?, ?, ?)''', (user.user_id, 'Deposit', amount, timestamp))
        conn.commit()
        conn.close()
        return f"Deposit successful {amount} added to your account"

    def withdraw(self, card_number, amount):
        conn = self.connect_db()
        cursor = conn.cursor()

        user = self.UserDao.get_user_by_card(card_number)
        if not user:
            conn.close()
            return "User not found"

        current_balance = self.UserDao.get_balance(card_number)
        print(f"[DEBUG] Текущий баланс перед депозитом: {current_balance}")
        if current_balance < amount:
            conn.close()
            return "Insufficient funds"

        new_balance = current_balance - amount
        print(f"[DEBUG] Новый баланс после депозита: {new_balance}")

        cursor.execute("UPDATE users SET balance = ? WHERE card_number = ?", (new_balance, card_number))

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''INSERT INTO transactions (user_id, transaction_type, amount, timestamp)
                            VALUES (?, ?, ?, ?)''', (user.user_id, 'withdraw', -amount, timestamp))

        conn.commit()
        conn.close()
        return f"Withdrawal successful {amount} withdrawn from your account"

    def transfer_funds(self, sender_card, receiver_card, amount):
        conn = self.connect_db()
        cursor = conn.cursor()

        try:
            sender = self.UserDao.get_user_by_card(sender_card)
            receiver = self.UserDao.get_user_by_card(receiver_card)

            if not sender or not receiver:
                return "Invalid card number(s)"

            sender_balance = self.UserDao.get_balance(sender_card)
            receiver_balance = self.UserDao.get_balance(receiver_card)
            print(f"[DEBUG] Текущий баланс отправителя: {sender_balance}")
            print(f"[DEBUG] Текущий баланс получателя: {receiver_balance}")

            if sender.get_balance() < amount:
                return "Insufficient funds"

            new_sender_balance = sender_balance - amount
            new_receiver_balance = receiver_balance + amount
            print(f"[DEBUG] Новый баланс отправителя: {new_sender_balance}")
            print(f"[DEBUG] Новый баланс получателя: {new_receiver_balance}")

            print(f"[DEBUG] Новый баланс отправителя: {new_sender_balance}")
            cursor.execute("UPDATE users SET balance = ? WHERE card_number = ?", (new_sender_balance, sender_card))
            cursor.execute("UPDATE users SET balance = ? WHERE card_number = ?", (new_receiver_balance, receiver_card))

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute('''INSERT INTO transactions (user_id, transaction_type, amount, timestamp)
                              VALUES (?, ?, ?, ?)''', (sender.user_id, 'transfer', -amount, now))

            cursor.execute('''INSERT INTO transactions (user_id, transaction_type, amount, timestamp)
                                VALUES (?, ?, ?, ?)''', (receiver.user_id, 'transfer', amount, now))

            conn.commit()
            return f"Transfer successful {amount} from {sender_card} to {receiver_card}"
        except Exception as e:
            conn.rollback()
            return f"Transfer failed: {str(e)}"
        finally:
            conn.close()

    def delete_all_transactions(self):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute(''' DELETE FROM transactions''')
        cursor.execute(''' DELETE FROM sqlite_sequence WHERE name = 'transactions' ''')
        conn.commit()
        conn.close()