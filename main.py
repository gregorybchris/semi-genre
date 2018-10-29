from api.soundcloud_client import SoundCloudClient
from api.mysql_client import MySQLClient
from pprint import pprint

sc_client = SoundCloudClient()
mysql_client = MySQLClient()

user = sc_client.fetch_user(6)
pprint(user)

user = {'user_id': 1, 'name': 'Joe'}
mysql_client.insert_user(**user)