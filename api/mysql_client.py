import MySQLdb
from configs.db_config import HOST, USERNAME, PASSWORD, DATABASE


class MySQLClient():
    def __init__(self):
        self._db = MySQLdb.connect(host=HOST, user=USERNAME, passwd=PASSWORD, db=DATABASE)

    def select_user(self, user_id):
        cursor = self._db.cursor(MySQLdb.cursors.DictCursor)
        query = "SELECT * FROM users WHERE user_id = %(id)s;"
        query_params = {'id': user_id}
        result = cursor.execute(query, query_params)
        if result != 1:
            raise ValueError(f"User with id={user_id} not found")
        user = cursor.fetchone()
        return user

    def select_users(self):
        cursor = self._db.cursor(MySQLdb.cursors.DictCursor)
        query = "SELECT * FROM users;"
        result = cursor.execute(query)
        if result != 1:
            raise ValueError(f"No users found")
        users = list(cursor.fetchall())
        return users

    def select_track(self, track_id):
        cursor = self._db.cursor(MySQLdb.cursors.DictCursor)
        query = "SELECT * FROM tracks WHERE track_id = %(id)s;"
        query_params = {'id': track_id}
        result = cursor.execute(query, query_params)
        if result != 1:
            raise ValueError(f"Track with id={track_id} not found")
        track = cursor.fetchone()
        return track

    def select_user_favorites(self, user_id):
        cursor = self._db.cursor(MySQLdb.cursors.DictCursor)
        query = "SELECT * FROM user_favorites WHERE user_id = %(id)s;"
        query_params = {'id': user_id}
        result = cursor.execute(query, query_params)
        if result != 1:
            raise ValueError(f"Favorites for user with id={user_id} not found")
        tracks = list(cursor.fetchall())
        return tracks

    def select_user_tracks(self, user_id):
        cursor = self._db.cursor(MySQLdb.cursors.DictCursor)
        query = "SELECT * FROM tracks WHERE artist_id = %(id)s;"
        query_params = {'id': user_id}
        result = cursor.execute(query, query_params)
        if result != 1:
            raise ValueError(f"Tracks for user with id={user_id} not found")
        tracks = list(cursor.fetchall())
        return tracks

    def insert_user(self, **kwargs):
        if 'user_id' not in kwargs:
            raise ValueError("Keyword argument 'user_id' needed to create user")
        
        cursor = self._db.cursor(MySQLdb.cursors.DictCursor)
        columns = kwargs.keys()
        values = kwargs.values()
        
        # TODO: Figure out how to insert arbitrarily many values

        columns_string = ", ".join(columns)
        values_string = ", ".join(values)
        query = f"INSERT INTO users (%(columns)s) VALUES (%(values)s);"
        query_params = {'columns': columns_string, 'values': values_string}

        print(query)
        # result = cursor.execute(query, query_params)
        # self._db.commit()
        
        # return True if result == 1 else False


    # def insert_track(self, track):
    #     field_names = [key for key in vars(track)]
    #     field_values = [track[field_name] for field_name in field_names]
        
    #     params = ", ".join(["%s" for _ in field_names])
    #     query = "INSERT INTO tracks (" + ", ".join(field_names) + ") VALUES (%s);" % params
        
    #     result = -1
    #     try:
    #         result = cursor.execute(query, field_values)
    #         db.commit()
    #     except MySQLdb.IntegrityError as error:
    #         print("Track exists in database")
    #     return True if result == 1 else False


    # def insert_favorite(self, favorite):
    #     field_names = [key for key in vars(favorite)]
    #     field_values = [favorite[field_name] for field_name in field_names]
        
    #     params = ", ".join(["%s" for _ in field_names])
    #     query = "INSERT INTO favorites (" + ", ".join(field_names) + ") VALUES (%s);" % params
        
    #     result = -1
    #     try:
    #         result = cursor.execute(query, field_values)
    #         db.commit()
    #     except MySQLdb.IntegrityError as error:
    #         print("Favorite exists in database")
    #     return True if result == 1 else False