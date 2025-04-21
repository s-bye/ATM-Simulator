from classes.dao.transactionsDAO import TransactionDAO
from classes.dao.userDAO import UserDAO
from classes.dao.loggingDAO import LoggingDAO

class Model:
    def __init__(self):
        self.transaction_dao = TransactionDAO()
        self.user_dao = UserDAO()
        self.logging_dao = LoggingDAO()

    def deposit(self, card_number, amount):
        user = self.user_dao.get_user_by_card(card_number)
        if not user:
            return "User not found"

        current_balance = self.user_dao.get_balance(card_number)
        new_balance = current_balance + amount

        self.transaction_dao.add_transaction(user.user_id, 'Deposit', amount)
        self.user_dao.update_balance(user.user_id, new_balance)

        self.logging_dao.add_log(user.user_id, f"Deposited {amount}")

        return f"Deposit of {amount} successful"

    def withdraw(self, card_number, amount):
        user = self.user_dao.get_user_by_card(card_number)
        if not user:
            return "User not found"

        current_balance = self.user_dao.get_balance(card_number)
        if current_balance < amount:
            return "Insufficient funds"

        new_balance = current_balance - amount

        self.transaction_dao.add_transaction(user.user_id, 'Withdraw', -amount)
        self.user_dao.update_balance(user.user_id, new_balance)

        self.logging_dao.add_log(user.user_id, f"Withdrew {amount}")

        return f"Withdrawal of {amount} successful"

    def transfer(self, sender_card, receiver_card, amount):
        sender = self.user_dao.get_user_by_card(sender_card)
        receiver = self.user_dao.get_user_by_card(receiver_card)

        if not sender or not receiver:
            return "Invalid card number(s)"

        sender_balance = self.user_dao.get_balance(sender_card)
        if sender_balance < amount:
            return "Insufficient funds"

        receiver_balance = self.user_dao.get_balance(receiver_card)
        new_sender_balance = sender_balance - amount
        new_receiver_balance = receiver_balance + amount

        self.transaction_dao.add_transaction(sender.user_id, 'Transfer', -amount)
        self.transaction_dao.add_transaction(receiver.user_id, 'Transfer', amount)

        self.user_dao.update_balance(sender.user_id, new_sender_balance)
        self.user_dao.update_balance(receiver.user_id, new_receiver_balance)

        self.logging_dao.add_log(sender.user_id, f"Transferred {amount} to {receiver_card}")
        self.logging_dao.add_log(receiver.user_id, f"Received {amount} from {sender_card}")

        return f"Transfer of {amount} from {sender_card} to {receiver_card} successful"

    def delete_logs_for_user(self, user_id):
        self.logging_dao.delete_logs_by_user_id(user_id)

    def delete_all_users(self):
        self.user_dao.delete_all_users()

    def delete_all_transactions(self):
        self.transaction_dao.delete_all_transactions()

    def delete_all_logs(self):
        self.logging_dao.delete_all_logs()

    def check_pin(self, card_number, pin):
        user = self.user_dao.get_user_by_card(card_number)
        if user and user.get_pin_code() == pin:
            return True
        return False

    def get_user_by_card(self, card_number):
        return self.user_dao.get_user_by_card(card_number)

    def add_log(self, user_id, action):
        self.logging_dao.add_log(user_id, action)
