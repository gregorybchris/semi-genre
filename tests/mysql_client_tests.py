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

    # def test_get_track(self):
    #     track_id = 0
    #     track = self._client.get_track(track_id)
    #     self.assertIsNotNone(track)

    # def test_select_user_favorites(self):
    #     user_id = 0
    #     tracks = self._client.select_user_favorites(user_id)
    #     self.assertIsNotNone(tracks)

    # def test_select_user_tracks(self):
    #     user_id = 0
    #     tracks = self._client.select_user_tracks(user_id)
    #     self.assertIsNotNone(tracks)


if __name__ == '__main__':
    unittest.main()
