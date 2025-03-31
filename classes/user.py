import sqlite3

class UserAuthentication:
    def __init__(self, card_number, pin_code):
        self.card_number = card_number
        self.pin_code = pin_code

    def authenticate(self):
        with sqlite3.connect("bank_database.sqlite") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT card_number, pin_code FROM user_authentication WHERE card_number = ? AND pin_code = ?", (self.card_number, self.pin_code))
            row = cursor.fetchone()
            if row is None:
                raise ValueError("Incorrect card number or PIN code")
            return True