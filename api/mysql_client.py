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
        return self._session.query(Track).get(track_id)

    def get_tracks(self, track_ids):
        return self._session.query(Track).filter(Track.track_id.in_(track_ids)).all()

    def insert_track(self, track):
        try:
            self._session.add(track)
            self._session.commit()
        except IntegrityError:
            self._session.rollback()
            raise ValueError(f"Track already exists with id={track.track_id}")

    def insert_tracks(self, tracks):
        self._session.bulk_save_objects(tracks)
        self._session.commit()

    # Favorite Operations

    def get_favorite(self, favorite_id):
        return self._session.query(Favorite).get(favorite_id)

    def get_favorites(self, favorite_ids):
        return self._session.query(Favorite).filter(Favorite.favorite_id.in_(favorite_ids)).all()

    def insert_favorite(self, favorite):
        try:
            self._session.add(favorite)
            self._session.commit()
        except IntegrityError:
            self._session.rollback()
            raise ValueError(f"Favorite already exists with id={favorite.favorite_id}")

    def insert_favorites(self, favorites):
        self._session.bulk_save_objects(favorites)
        self._session.commit()

