import unittest
from api.soundcloud_client import SoundCloudClient

class SoundCloudClientTests(unittest.TestCase):
    def setUp(self):
        self._client = SoundCloudClient()

    def test_fetch_user(self):
        user_id = 6
        user = self._client.fetch_user(user_id)
        self.assertIsNotNone(user)
    
    def test_fetch_user_missing(self):
        user_id = 0
        with self.assertRaises(ValueError):
            self._client.fetch_user(user_id)

    def test_fetch_track(self):
        track_id = 54462448
        track = self._client.fetch_track(track_id)
        self.assertIsNotNone(track)
    
    def test_fetch_user_favorites(self):
        user_id = 6
        tracks = self._client.fetch_user_favorites(user_id)
        self.assertIsNotNone(tracks)
    
    def test_fetch_user_tracks(self):
        user_id = 6
        tracks = self._client.fetch_user_tracks(user_id)
        self.assertIsNotNone(tracks)

if __name__ == '__main__':
    unittest.main()