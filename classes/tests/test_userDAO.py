import unittest
import os
from classes.dao.userDAO import UserDAO
from classes.user import User


class TestUserDAO(unittest.TestCase):
    def setUp(self):
        # Get the absolute path to the bank_database.sqlite in tests/
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "bank_database.sqlite"))
        self.user_dao = UserDAO(db_file=db_path)
        # Clean up users table before each test
        self.user_dao.delete_all_users()

    def tearDown(self):
        # Clean up after each test
        self.user_dao.delete_all_users()

    def test_add_user(self):
        user = User(None, "John Doe", "1234567891234567", "1234", 1000.0)
        self.user_dao.add_user(user)
        retrieved_user = self.user_dao.get_user_by_card("1234567891234567")
        self.assertEqual(retrieved_user.full_name, "John Doe")
        self.assertEqual(retrieved_user.get_balance(), 1000.0)

    def test_get_user_by_card(self):
        user = User(None, "Jane Doe", "9876543219876543", "5678", 500.0)
        self.user_dao.add_user(user)
        retrieved_user = self.user_dao.get_user_by_card("9876543219876543")
        self.assertEqual(retrieved_user.full_name, "Jane Doe")
        self.assertIsNone(self.user_dao.get_user_by_card("0000000000000000"))

    def test_update_balance(self):
        user = User(None, "Alice Smith", "1111222233334444", "4321", 2000.0)
        self.user_dao.add_user(user)
        retrieved_user = self.user_dao.get_user_by_card("1111222233334444")
        self.user_dao.update_balance(retrieved_user.user_id, 2500.0)
        updated_user = self.user_dao.get_user_by_card("1111222233334444")
        self.assertEqual(updated_user.get_balance(), 2500.0)

    def test_check_pin(self):
        user = User(None, "Bob Brown", "5555666677778888", "9999", 3000.0)
        self.user_dao.add_user(user)
        self.assertTrue(self.user_dao.check_pin("5555666677778888", "9999"))
        self.assertFalse(self.user_dao.check_pin("5555666677778888", "0000"))

    def test_delete_user(self):
        user = User(None, "Charlie Green", "9999000011112222", "1111", 4000.0)
        self.user_dao.add_user(user)
        retrieved_user = self.user_dao.get_user_by_card("9999000011112222")
        self.user_dao.delete_user(retrieved_user.user_id)
        self.assertIsNone(self.user_dao.get_user_by_card("9999000011112222"))

if __name__ == "__main__":
    unittest.main()