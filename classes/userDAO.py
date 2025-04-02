import sqlite3
from user import User  # Assuming User class is in user.py


class UserDAO:
    def __init__(self, db_path="bank_database.sqlite"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def add_user(self, user):
        self.cursor.execute("""
            INSERT INTO users (full_name, card_number, pin_code, balance)
            VALUES (?, ?, ?, ?)
        """, (user.full_name, user.card_number, user.get_pin_code(), user.get_balance()))
        self.conn.commit()

    def get_user_by_card(self, card_number):
        self.cursor.execute("SELECT * FROM users WHERE card_number = ?", (card_number,))
        row = self.cursor.fetchone()
        return User(*row) if row else None

    def update_balance(self, user_id, new_balance):
        self.cursor.execute("UPDATE users SET balance = ? WHERE user_id = ?", (new_balance, user_id))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

