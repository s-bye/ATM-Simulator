import unittest
import os
from classes.dao.transactionsDAO import TransactionDAO
from classes.user import User
from classes.transactions import Transaction


class TestTransactionDAO(unittest.TestCase):
    def setUp(self):
        # Get the absolute path to the bank_database.sqlite in tests/
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\Users\User\Documents\Python\oop_learning\ATM-Simulator\bank_database.sqlite"))
        self.transaction_dao = TransactionDAO(db_file=db_path)
        # Clean up transactions and users tables before each test
        self.transaction_dao.delete_all_transactions()
        self.transaction_dao.UserDao.delete_all_users()
        # Add a test user
        self.user = User(None, "Imanbek Mashrapov", "1234567891234567", "1234", 1000.0)
        self.transaction_dao.UserDao.add_user(self.user)

    def tearDown(self):
        # Clean up after each test
        self.transaction_dao.delete_all_transactions()
        self.transaction_dao.UserDao.delete_all_users()

    def test_add_transaction(self):
        user = self.transaction_dao.UserDao.get_user_by_card("1234567891234567")
        self.transaction_dao.add_transaction(user.user_id, "Deposit", 500.0)
        transactions = self.transaction_dao.get_transactions_by_user_id(user.user_id)
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].transaction_type, "Deposit")
        self.assertEqual(transactions[0].get_amount(), 500.0)

    def test_deposit(self):
        result = self.transaction_dao.deposit("1234567891234567", 300.0)
        self.assertEqual(result, "Deposit successful 300.0 added to your account")
        user = self.transaction_dao.UserDao.get_user_by_card("1234567891234567")
        self.assertEqual(user.get_balance(), 1300.0)

    def test_withdraw(self):
        result = self.transaction_dao.withdraw("1234567891234567", 200.0)
        self.assertEqual(result, "Withdrawal successful 200.0 withdrawn from your account")
        user = self.transaction_dao.UserDao.get_user_by_card("1234567891234567")
        self.assertEqual(user.get_balance(), 800.0)

    def test_withdraw_insufficient_funds(self):
        result = self.transaction_dao.withdraw("1234567891234567", 2000.0)
        self.assertEqual(result, "Insufficient funds")
        user = self.transaction_dao.UserDao.get_user_by_card("1234567891234567")
        self.assertEqual(user.get_balance(), 1000.0)

    def test_transfer_funds(self):
        receiver = User(None, "Receiver User", "9876543219876543", "5678", 500.0)
        self.transaction_dao.UserDao.add_user(receiver)
        result = self.transaction_dao.transfer_funds("1234567891234567", "9876543219876543", 300.0)
        self.assertEqual(result, "Transfer successful 300.0 from 1234567891234567 to 9876543219876543")
        sender = self.transaction_dao.UserDao.get_user_by_card("1234567891234567")
        receiver = self.transaction_dao.UserDao.get_user_by_card("9876543219876543")
        self.assertEqual(sender.get_balance(), 700.0)
        self.assertEqual(receiver.get_balance(), 800.0)

    def test_get_transactions_by_user_id(self):
        user = self.transaction_dao.UserDao.get_user_by_card("1234567891234567")
        self.transaction_dao.add_transaction(user.user_id, "Deposit", 400.0)
        self.transaction_dao.add_transaction(user.user_id, "Withdrawal", -100.0)
        transactions = self.transaction_dao.get_transactions_by_user_id(user.user_id)
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0].transaction_type, "Withdrawal")  # Ordered by timestamp DESC


if __name__ == "__main__":
    unittest.main()
