from api.soundcloud_client import SoundCloudClient
from api.mysql_client import MySQLClient
from model.mapper import ModelMapper

from config.sc_config import CLIENT_ID
from config.db_config import HOST, USER, PASS, DATABASE

sc_client = SoundCloudClient(CLIENT_ID)
mysql_client = MySQLClient(HOST, USER, PASS, DATABASE)
mapper = ModelMapper()


def save_user(user_id):
    try:
        # Fetch a user
        user_dict = sc_client.fetch_user(user_id)
        user = mapper.create_user(user_dict)
        try:
            mysql_client.insert_user(user)
            print(f"User Added: {user_id}")
        except ValueError:
            print(f"User Exists: {user_id}")

        try:
            # Fetch the favorite tracks of the user
            track_dicts = sc_client.fetch_user_favorites(user_id)
            tracks = [mapper.create_track(t) for t in track_dicts]
            for track in tracks:
                # Fetch the artist for the favorite track
                artist_dict = sc_client.fetch_user(track.artist_id)
                artist = mapper.create_user(artist_dict)
                try:
                    mysql_client.insert_user(artist)
                    print(f"Artist Added: {artist.user_id}")
                except ValueError:
                    pass

                try:
                    mysql_client.insert_track(track)
                    print(f"Track Added: {track.track_id}")
                    try:
                        favorite_dict = {
                            'user_id': user_id,
                            'track_id': track.track_id
                        }
                        favorite = mapper.create_favorite(favorite_dict)
                        mysql_client.insert_favorite(favorite)
                    except ValueError:
                        pass
                except ValueError:
                    pass
        except ValueError:
            pass
    except ValueError:
        print(f"{user_id}: User Not Found")


user_ids = range(0, 10000)
for user_id in user_ids:
    save_user(user_id)
