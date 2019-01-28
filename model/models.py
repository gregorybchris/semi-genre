from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    description = Column(String)
    city = Column(String)
    country = Column(String)
    avatar_url = Column(String)
    last_modified = Column(DateTime)
    permalink = Column(String)
    permalink_url = Column(String)
    plan = Column(String)
    username = Column(String)
    website = Column(String)
    playlist_count = Column(Integer)
    public_favorites_count = Column(Integer)
    reposts_count = Column(Integer)
    track_count = Column(Integer)
    followers_count = Column(Integer)
    followings_count = Column(Integer)

    tracks = relationship('Track', backref='user')
    favorites = relationship('Favorite', backref='user')

    def __str__(self):
        return ("<User("
                f"user_id={self.user_id}, "
                f"username='{self.username}', "
                f"permalink_url='{self.permalink_url}'"
                ")>")


class Track(Base):
    __tablename__ = 'tracks'

    track_id = Column(Integer, primary_key=True)
    artist_id = Column(Integer, ForeignKey('users.user_id'))
    artwork_url = Column(String)
    attachments_uri = Column(String)
    bpm = Column(Integer)
    comment_count = Column(Integer)
    commentable = Column(Boolean)
    created_at = Column(DateTime)
    description = Column(String)
    download_count = Column(Integer)
    downloadable = Column(Boolean)
    duration = Column(Integer)
    embeddable_by = Column(String)
    favoritings_count = Column(Integer)
    genre = Column(String)
    key_signature = Column(String)
    label_id = Column(Integer)
    label_name = Column(String)
    last_modified = Column(DateTime)
    license = Column(String)
    original_content_size = Column(Integer)
    original_format = Column(String)
    permalink = Column(String)
    permalink_url = Column(String)
    playback_count = Column(Integer)
    purchase_title = Column(String)
    purchase_url = Column(String)
    release_date = Column(DateTime)
    release_day = Column(Integer)
    release_month = Column(Integer)
    release_year = Column(Integer)
    sharing = Column(String)
    state = Column(String)
    stream_url = Column(String)
    streamable = Column(Boolean)
    tag_list = Column(String)
    title = Column(String)
    track_type = Column(String)
    video_url = Column(String)
    waveform_url = Column(String)

    favorites = relationship('Favorite', backref='track')

    def __str__(self):
        return ("<Track("
                f"track_id={self.track_id}, "
                f"artist_id={self.artist_id}, "
                f"title='{self.title}', "
                f"permalink_url='{self.permalink_url}'"
                ")>")


class Favorite(Base):
    __tablename__ = 'favorites'

    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    track_id = Column(Integer, ForeignKey('tracks.track_id'))

    def __str__(self):
        return ("<Favorite("
                f"favorite_id={self.favorite_id}, "
                f"user_id={self.user_id}, "
                f"track_id={self.track_id}"
                ")>")
