from classes.user import User
from classes.dao.baseDAO import BaseDAO


class UserDAO(BaseDAO):
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

    def update_balance(self, user_id, new_balance):
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET balance = ? WHERE user_id = ?", (new_balance, user_id))
        conn.commit()
        conn.close()
