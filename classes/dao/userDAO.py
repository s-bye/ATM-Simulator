from classes.user import User
from classes.dao.baseDAO import BaseDAO


class UserDAO(BaseDAO):
    def __init__(self, db_file="bank_database.sqlite"):
        super().__init__(db_file)

    def add_user(self, user):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (full_name, card_number, pin_code, balance)
            VALUES (?, ?, ?, ?)
        """, (user.full_name, user.card_number, user.get_pin_code(), user.get_balance()))

        conn.commit()
        conn.close()

    def get_user_by_card(self, card_number):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE card_number = ?", (card_number,))
        row = cursor.fetchone()

        conn.close()
        return User(*row) if row else None

    def get_user_by_id(self, user_id):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        conn.close()

        return [User(*row) for row in rows]

    def update_balance(self, user_id, new_balance):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET balance = ? WHERE user_id = ?", (new_balance, user_id))
        conn.commit()
        conn.close()

    def check_pin(self, card_number, input_pin):
        user = self.get_user_by_card(card_number)
        return user and user.get_pin_code() == input_pin

    def delete_user(self, user_id):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute('''DElETE FROM users WHERE user_id = ? ''', (user_id,))
        conn.commit()
        conn.close()

    def get_balance(self, card_number):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT balance FROM users WHERE card_number = ?", (card_number,))
        row = cursor.fetchone()
        conn.close()

        return float(row[0]) if row else None

    def delete_all_users(self):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute(''' DELETE FROM users''')
        cursor.execute(''' DELETE FROM sqlite_sequence WHERE name = 'users' ''')
        conn.commit()
        conn.close()