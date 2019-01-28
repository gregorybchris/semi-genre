import unittest
from api.mysql_client import MySQLClient
from config.db_config import HOST, USER, PASS, DATABASE


class MySQLClientTests(unittest.TestCase):
    def setUp(self):
        self._client = MySQLClient(HOST, USER, PASS, DATABASE)

    # User Operations

    def test_get_user(self):
        user_id = 0
        user = self._client.get_user(user_id)
        self.assertIsNotNone(user)

    def test_get_users(self):
        user_ids = [0]
        users = self._client.get_users(user_ids)
        print(users)
        self.assertIsNotNone(users)

    # Track Operations

    # Favorite Operations


if __name__ == '__main__':
    unittest.main()
