from api.soundcloud_client import SoundCloudClient
from api.mysql_client import MySQLClient
from model.mapper import ModelMapper

from config.sc_config import CLIENT_ID
from config.db_config import HOST, USER, PASS, DATABASE

sc_client = SoundCloudClient(CLIENT_ID)
mysql_client = MySQLClient(HOST, USER, PASS, DATABASE)
mapper = ModelMapper()

user_ids = range(40)
for user_id in user_ids:
    try:
        user_dict = sc_client.fetch_user(user_id)
        user = mapper.create_user(user_dict)
        try:
            mysql_client.insert_user(user)
            print(f"{user_id}: Created")
        except ValueError as e:
            print(f"{user_id}: Record Exists")
        
        
    except ValueError as e:
        print(f"{user_id}: Not Found")

# vs = mysql_client.get_existing_user_ids(user_ids)
# print(vs)

# user_dict = sc_client.fetch_user(6)
# print(user_dict['last_name'])