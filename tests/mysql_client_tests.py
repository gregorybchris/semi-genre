import unittest
from api.mysql_client import MySQLClient

class SoundCloudClientTests(unittest.TestCase):
    def setUp(self):
        self._client = MySQLClient()

    def test_select_user(self):
        user_id = 0
        user = self._client.select_user(user_id)
        self.assertIsNotNone(user)
    
    def test_select_users(self):
        users = self._client.select_users()
        self.assertIsNotNone(users)
    
    def test_select_track(self):
        track_id = 0
        track = self._client.select_track(track_id)
        self.assertIsNotNone(track)

    def test_select_user_favorites(self):
        user_id = 0
        tracks = self._client.select_user_favorites(user_id)
        self.assertIsNotNone(tracks)
    
    def test_select_user_tracks(self):
        user_id = 0
        tracks = self._client.select_user_tracks(user_id)
        self.assertIsNotNone(tracks)

if __name__ == '__main__':
    unittest.main()