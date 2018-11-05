import soundcloud
from requests.exceptions import ConnectionError, HTTPError


class SoundCloudClient():
    def __init__(self, client_id):
        self._client = soundcloud.Client(client_id=client_id)

    def fetch_user(self, user_id):
        try:
            query_url = f"/users/{user_id}"
            user = self._client.get(query_url).obj
        except HTTPError:
            self._raise_not_found('user', user_id)
        except ConnectionError:
            raise ValueError("Could not connect to SoundCloud")
        return user

    def fetch_track(self, track_id):
        try:
            query_url = f"/tracks/{track_id}"
            track = self._client.get(query_url).obj
        except HTTPError:
            self._raise_not_found('track', track_id)
        except ConnectionError:
            raise ValueError("Could not connect to SoundCloud")
        return track

    def fetch_user_favorites(self, user_id):
        try:
            query_url = f"/users/{user_id}/favorites"
            track_records = self._client.get(query_url).data
        except HTTPError:
            self._raise_not_found('favorites', user_id, parent='user')
        except ConnectionError:
            raise ValueError("Could not connect to SoundCloud")
        tracks = [rec.obj for rec in track_records]
        return tracks

    def fetch_user_tracks(self, user_id):
        try:
            query_url = f"/users/{user_id}/tracks"
            track_records = self._client.get(query_url).data
        except HTTPError:
            self._raise_not_found('tracks', user_id, parent='user')
        except ConnectionError:
            self._raise_no_conn()
        tracks = [rec.obj for rec in track_records]
        return tracks

    def _raise_not_found(self, model, record_id, parent=''):
        raise ValueError(f"Could not find {model} with"
                         f"{parent} id={record_id}")

    def _raise_no_conn(self):
        raise ValueError("Could not connect to SoundCloud")
