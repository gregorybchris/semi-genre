from requests.exceptions import HTTPError
import soundcloud
from configs.sc_config import CLIENT_ID

class SoundCloudClient():
	def __init__(self):
		self._client = soundcloud.Client(client_id=CLIENT_ID)

	def fetch_user(self, user_id):
		try:
			user = self._client.get(f"/users/{user_id}").obj
		except HTTPError:
			raise ValueError(f"Could not find user with id={user_id}")
		return user

	def fetch_track(self, track_id):
		try:
			track = self._client.get(f"/tracks/{track_id}").obj
		except HTTPError:
			raise ValueError(f"Could not find track with id={track_id}")
		return track

	def fetch_user_favorites(self, user_id):
		try:
			track_records = self._client.get(f"/users/{user_id}/favorites").data
		except HTTPError:
			raise ValueError(f"Could not find favorites of user with id={user_id}")
		tracks = [rec.obj for rec in track_records]
		return tracks
	
	def fetch_user_tracks(self, user_id):
		try:
			track_records = self._client.get(f"/users/{user_id}/tracks").data
		except HTTPError:
			raise ValueError(f"Could not find tracks of user with id={user_id}")
		tracks = [rec.obj for rec in track_records]
		return tracks