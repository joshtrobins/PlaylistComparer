import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
from Playlist import Playlist
from Song import Song


# https://spotipy.readthedocs.io/en/2.16.1/
def scrape(client_id, client_secret, username):
    playlists = []
    client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))
    generated_playlists = client.user_playlists(username)
    for generated_playlist in generated_playlists["items"]:
        playlist = Playlist(generated_playlist["name"])
        offset = 0
        while True:
            generated_tracks_container = client.playlist_items(generated_playlist["id"], offset=offset)
            generated_tracks = generated_tracks_container["items"]
            generated_tracks_count = len(generated_tracks)
            if len(generated_tracks) == 0:
                break
            for generated_track_container in generated_tracks:
                generated_track = generated_track_container["track"]
                generated_track_id = generated_track["uri"] if generated_track["id"] is None else generated_track["id"]
                playlist.songs.append(
                    Song(
                        generated_track["name"],
                        generated_track["artists"][0]["name"],
                        generated_track["album"]["name"],
                        generated_track_id))
            offset = offset + generated_tracks_count
        playlists.append(playlist)

    return playlists
