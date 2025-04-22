import unittest
import os
from classes.dao.loggingDAO import LoggingDAO
from classes.logging import Logging


class TestLoggingDAO(unittest.TestCase):
    def setUp(self):
        # Get the absolute path to the bank_database.sqlite in tests/
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\Users\User\Documents\Python\oop_learning\ATM-Simulator\bank_database.sqlite"))
        self.log_dao = LoggingDAO(db_file=db_path)
        # Clean up logs table before each test
        self.log_dao.delete_all_logs()

    def tearDown(self):
        # Clean up after each test
        self.log_dao.delete_all_logs()

    def test_add_log(self):
        self.log_dao.add_log(1, "Login")
        logs = self.log_dao.get_logs_by_user_id(1)
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0].action, "Login")
        self.assertEqual(logs[0].user_id, 1)

    def test_get_logs_by_user_id(self):
        self.log_dao.add_log(2, "Deposit")
        self.log_dao.add_log(2, "Withdrawal")
        self.log_dao.add_log(3, "Login")
        logs = self.log_dao.get_logs_by_user_id(2)
        self.assertEqual(len(logs), 2)
        self.assertEqual(logs[0].action, "Withdrawal")  # Ordered by timestamp DESC
        self.assertEqual(logs[1].action, "Deposit")

    def test_get_all_logs(self):
        self.log_dao.add_log(1, "Login")
        self.log_dao.add_log(2, "Deposit")
        all_logs = self.log_dao.get_all_logs()
        self.assertEqual(len(all_logs), 2)

    def test_delete_logs_by_user_id(self):
        self.log_dao.add_log(1, "Login")
        self.log_dao.add_log(1, "Logout")
        self.log_dao.add_log(2, "Deposit")
        self.log_dao.delete_logs_by_user_id(1)
        logs = self.log_dao.get_logs_by_user_id(1)
        self.assertEqual(len(logs), 0)
        logs = self.log_dao.get_logs_by_user_id(2)
        self.assertEqual(len(logs), 1)

    def test_delete_all_logs(self):
        self.log_dao.add_log(1, "Login")
        self.log_dao.add_log(2, "Deposit")
        self.log_dao.delete_all_logs()
        all_logs = self.log_dao.get_all_logs()
        self.assertEqual(len(all_logs), 0)


if __name__ == "__main__":
    unittest.main()
