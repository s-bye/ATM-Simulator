import unittest
from classes.user import User
from classes.transactions import Transaction
from classes.dao.userDAO import UserDAO
from classes.user import User
from classes.logging import Logging
import datetime
from classes.dao.loggingDAO import LoggingDAO
from classes.dao.transactionsDAO import TransactionDAO


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(user_id=1, full_name="John Doe", card_number="1234567890123456", pin_code="1234", balance=1000.0)
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.full_name, "John Doe")
        self.assertEqual(user.card_number, "1234567890123456")
        self.assertEqual(user.get_balance(), 1000.0)

    def test_set_balance(self):
        user = User(user_id=1, full_name="John Doe", card_number="1234567890123456", pin_code="1234", balance=1000.0)
        user.set_balance(1500.0)
        self.assertEqual(user.get_balance(), 1500.0)

    def test_set_pin_code(self):
        user = User(user_id=1, full_name="John Doe", card_number="1234567890123456", pin_code="1234", balance=1000.0)
        user.set_pin_code("5678")
        self.assertEqual(user.get_pin_code(), "5678")


class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        transaction = Transaction(transaction_id=1, user_id=1, transaction_type="Deposit", amount=500.0, timestamp="2025-04-22 12:00:00")
        self.assertEqual(transaction.transaction_id, 1)
        self.assertEqual(transaction.user_id, 1)
        self.assertEqual(transaction.transaction_type, "Deposit")
        self.assertEqual(transaction.get_amount(), 500.0)
        self.assertEqual(transaction.timestamp, "2025-04-22 12:00:00")

    def test_set_amount(self):
        transaction = Transaction(transaction_id=1, user_id=1, transaction_type="Deposit", amount=500.0, timestamp="2025-04-22 12:00:00")
        transaction.set_amount(1000.0)
        self.assertEqual(transaction.get_amount(), 1000.0)


class TestLogging(unittest.TestCase):

    def setUp(self):
        self.log = Logging(log_id=1, user_id=123, action="Deposit")

    def test_logging_initialization(self):
        self.assertEqual(self.log.log_id, 1)
        self.assertEqual(self.log.user_id, 123)
        self.assertEqual(self.log.action, "Deposit")

    def test_repr(self):
        expected_repr = f"Logging(log_id={self.log.log_id}, user_id={self.log.user_id}, action='{self.log.action}', timestamp='{self.log.timestamp}')"
        self.assertEqual(repr(self.log), expected_repr)

    def test_update_action(self):
        new_action = "Withdrawal"
        self.log.action = new_action
        self.assertEqual(self.log.action, new_action)

class TestUserDAO(unittest.TestCase):
    def setUp(self):
        self.user_dao = UserDAO()
        self.user = User(None, full_name="John Doe", card_number="1234567890123456", pin_code="1234", balance=1000.0)
        self.user_dao.add_user(self.user)
    def test_add_user(self):
        user = User(None, full_name="Jane Doe", card_number="6543210987654321", pin_code="5678", balance=2000.0)
        self.user_dao.add_user(user)
        retrieved_user = self.user_dao.get_user_by_card("6543210987654321")
        self.assertEqual(retrieved_user.full_name, "Jane Doe")
    def test_get_user_by_card(self):
        retrieved_user = self.user_dao.get_user_by_card("1234567890123456")
        self.assertEqual(retrieved_user.full_name, "John Doe")
        self.assertEqual(retrieved_user.get_balance(), 1000.0)
    def test_check_pin(self):
        pin_ok = self.user_dao.check_pin("1234567890123456", "1234")
        self.assertTrue(pin_ok)
        pin_ok = self.user_dao.check_pin("1234567890123456", "wrong_pin")
        self.assertFalse(pin_ok)
    def test_delete_user(self):
        self.user_dao.delete_user(1)
        retrieved_user = self.user_dao.get_user_by_card("1234567890123456")
        self.assertIsNone(retrieved_user)
    def tearDown(self):
        self.user_dao.delete_user(self.user.user_id)

class TestTransactionDAO(unittest.TestCase):
    def setUp(self):
        self.user_dao = UserDAO()
        self.transaction_dao = TransactionDAO()
        self.user = User(None, full_name="John Doe", card_number="1234567890123456", pin_code="1234", balance=1000.0)
        self.user_dao.add_user(self.user)

    def test_add_transaction(self):
        self.transaction_dao.add_transaction(self.user.user_id, "Deposit", 500.0)
        transactions = self.transaction_dao.get_transactions_by_user_id(self.user.user_id)
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].transaction_type, "Deposit")
        self.assertEqual(transactions[0].get_amount(), 500.0)

    def tearDown(self):
        self.transaction_dao.delete_all_transactions()
        self.user_dao.delete_user(self.user.user_id)

class TestLoggingDAO(unittest.TestCase):
    def setUp(self):
        self.logging_dao = LoggingDAO()
        self.user = User(None, full_name="John Doe", card_number="1234567890123456", pin_code="1234", balance=1000.0)

    def test_add_log(self):
        self.logging_dao.add_log(self.user.user_id, "login")
        logs = self.logging_dao.get_logs_by_user_id(self.user.user_id)
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0].action, "login")

    def tearDown(self):
        self.logging_dao.delete_all_logs()


if __name__ == "__main__":
    unittest.main()






