from model.models import User, Track, Favorite
from datetime import datetime
import re

class ModelMapper:
    def __init__(self):
        self._user_map = {
            'id': 'user_id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'description': 'description',
            'city': 'city',
            'country': 'country',
            'avatar_url': 'avatar_url',
            'last_modified': 'last_modified',
            'permalink': 'permalink',
            'permalink_url': 'permalink_url',
            'plan': 'plan',
            'username': 'username',
            'website': 'website',
            'playlist_count': 'playlist_count',
            'public_favorites_count': 'public_favorites_count',
            'reposts_count': 'reposts_count',
            'track_count': 'track_count',
            'followers_count': 'followers_count',
            'followings_count': 'followings_count'
        }

        self._track_map = {
            'id': 'track_id',
            'user_id': 'artist_id',
            'artwork_url': 'artwork_url',
            'attachments_uri': 'attachments_uri',
            'bpm': 'bpm',
            'comment_count': 'comment_count',
            'commentable': 'commentable',
            'created_at': 'created_at',
            'description': 'description',
            'download_count': 'download_count',
            'downloadable': 'downloadable',
            'duration': 'duration',
            'embeddable_by': 'embeddable_by',
            'favoritings_count': 'favoritings_count',
            'genre': 'genre',
            'key_signature': 'key_signature',
            'label_id': 'label_id',
            'label_name': 'label_name',
            'last_modified': 'last_modified',
            'license': 'license',
            'original_content_size': 'original_content_size',
            'original_format': 'original_format',
            'permalink': 'permalink',
            'permalink_url': 'permalink_url',
            'playback_count': 'playback_count',
            'purchase_title': 'purchase_title',
            'purchase_url': 'purchase_url',
            'release_date': 'release_date',
            'release_day': 'release_day',
            'release_month': 'release_month',
            'release_year': 'release_year',
            'sharing': 'sharing',
            'state': 'state',
            'stream_url': 'stream_url',
            'streamable': 'streamable',
            'tag_list': 'tag_list',
            'title': 'title',
            'track_type': 'track_type',
            'video_url': 'video_url',
            'waveform_url': 'waveform_url'
        }

        self._favorite_map = {
            'favorite_id': 'favorite_id',
            'user_id': 'user_id',
            'track_id': 'track_id'
        }

        self._date_time_fields = [
            'created_at',
            'last_modified',
            'release_date'
        ]

        self._long_string_fields = {
            'description': 5000,
            'tag_list': 5000,
            'purchase_url': 5000
        }

    def create_user(self, user_dict):
        return self._dict_to_record(user_dict, self._user_map, User)

    def create_track(self, track_dict):
        return self._dict_to_record(track_dict, self._track_map, Track)

    def create_favorite(self, favorite_dict):
        return self._dict_to_record(favorite_dict, self._favorite_map, Favorite)

    def _dict_to_record(self, record_dict, record_map, record_class):
        mapped_attributes = dict()
        for k, v in record_dict.items():
            if isinstance(v, str):
                v = self._convert_ascii(v)
                v = self._string_clip(k, v)
            if k in self._date_time_fields:
                v = self._convert_datetime(v)
            if k in record_map:
                mapped_attributes[record_map[k]] = v
        return record_class(**mapped_attributes)

    def _convert_datetime(self, datetime_string):
        format_string = '%Y/%m/%d %H:%M:%S %z'
        return datetime.strptime(datetime_string, format_string)

    def _convert_ascii(self, text):
        return re.sub(r'[^\x00-\x7F]+', '?', text)

    def _string_clip(self, field, text):
        if field in self._long_string_fields:
            size = self._long_string_fields[field]
        else:
            size = 200

        if len(text) > size:
            return text[:size]
        return text
