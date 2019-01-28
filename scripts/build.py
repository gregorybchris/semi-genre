from api.mysql_client import MySQLClient
from scripts.graph import Graph
from config.db_config import HOST, USER, PASS, DATABASE
import numpy as np


def graph_from_user_ids(db, user_ids):
    # Create a graph of musical artists
    g = Graph()
    users = db.get_users(user_ids)
    for user in [u for u in users if u is not None]:
        # Get the data for all artists each user likes
        artists = []
        for favorite in user.favorites:
            track = db.get_track(favorite.track_id)
            genre = _genre_lumper(track.genre)
            if genre is not None:
                artist = db.get_user(track.artist_id)
                artists.append(artist)

                # Add the artist to the graph
                if not g.has_node(artist.user_id):
                    node_data = _create_node_data(artist, genre)
                    g.add_node(artist.user_id, node_data)
        
        # Add links between all artists
        artist_ids = list(set(artist.user_id for artist in artists))
        g.add_complete_links(artist_ids)
    return g


def _create_node_data(artist, genre):
    node_data = dict()
    node_data['url'] = artist.permalink_url,
    node_data['artist'] = artist.username
    node_data['country'] = artist.country
    node_data['genre'] = genre
    return node_data


def _genre_lumper(genre):
    if genre is None:
        return None
    
    genre = genre.strip().lower()
    if genre == '':
        return None

    lumper = [
        ('Electronic', ['electr', 'house', 'edm', 'techn', 'dubstep', 'dub',
                        'dance', 'dj', 'drum & bass', 'balearic', 'acid',
                        'trap', 'boiler room', 'wave', 'elektr', 'bass', 'step',
                        'synth', 'deep', 'future']),
        ('Hip-hop', ['hip-hop', 'hiphop', 'hip hop', 'rap']),
        ('RnB', ['rnb', 'soul', 'r&b']),
        ('Alternative', ['altern', 'indie']),
        ('Nature', ['natur', 'jungle']),
        ('Disco', ['disco', 'disko']),
        ('Ambient', ['ambient', 'dream', 'trance', 'psych']),
        ('Pop', ['pop']),
        ('Jazz', ['jazz']),
        ('Rock', ['rock']),
        ('Classical', ['classical', 'piano']),
        ('Spoken', ['podcast', 'storytelling']),
        ('Metal', ['metal']),
        ('Bossa Nova', ['bossa']),
        ('Latin', ['south america', 'latin']),
        ('Acoustic', ['fingerstyle', 'acoustic']),
        ('Reggae', ['reggae']),
        ('Experimental', ['experi']),
        ('Folk', ['folk']),
        ('Blues', ['blues']),
        ('Instrumental', ['instrumental']),
        ('Funk', ['funk'])
    ]
    for category, parts in lumper:
        for part in parts:
            if part in genre:
                if category == 'Electronic':
                    return None
                return category

    return None


def save_graph_to_file(graph, filename):
    with open(filename, 'w') as file:
        file.write(graph.to_json(min_weight=1))


if __name__ == "__main__":
    db = MySQLClient(HOST, USER, PASS, DATABASE)
    
    # user_ids = np.random.randint(low=6000, high=9000, size=500)
    # g = graph_from_user_ids(db, user_ids)
    # save_graph_to_file(g, '../viz/data/test.json')

    search_ids = list(range(100000))
    users = db.get_users(search_ids)
    existing_ids = set([u.user_id for u in users])
    for user_id in search_ids:
        if user_id in existing_ids:
            print("&", end="")
        else:
            print("_", end="")