from model.models import User, Track, Favorite
from sqlalchemy import create_engine
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import logging


class MySQLClient():
    def __init__(self, host, user, password, database):
        conn_str = f'mysql://{user}:{password}@{host}/{database}'
        engine = create_engine(conn_str, echo=False)
        self._session = sessionmaker(bind=engine)()

        logging_handler = logging.FileHandler('sqla.log')
        logger = logging.getLogger('sqlalchemy.engine')
        logger.setLevel(logging.INFO)
        logger.addHandler(logging_handler)

    # User Operations

    def get_existing_user_ids(self, user_ids):
        return self._session.query(exists().where(User.user_id in user_ids))

    def get_user(self, user_id):
        return self._session.query(User).get(user_id)

    def get_users(self, user_ids):
        return self._session.query(User).filter(User.user_id.in_(user_ids)).all()

    def insert_user(self, user):
        try:
            self._session.add(user)
            self._session.commit()
        except IntegrityError:
            self._session.rollback()
            raise ValueError(f"User already exists with id={user.user_id}")

    def insert_users(self, users):
        self._session.bulk_save_objects(users)
        self._session.commit()

    # Track Operations

    def get_track(self, track_id):
        pass

    def get_tracks(self, track_ids):
        pass

    def insert_track(self, track):
        pass

    def insert_tracks(self, tracks):
        pass

    # Favorite Operations

    def get_favorite(self, favorite_id):
        pass

    def get_favorites(self, favorite_ids):
        pass

    def insert_favorite(self, favorite):
        pass

    def insert_favorites(self, favorites):
        pass
