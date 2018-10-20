import gmusicapi
from Song import Song
from Playlist import Playlist


# https://unofficial-google-music-api.readthedocs.io/en/latest/reference/mobileclient.html
def scrape(username, password):
    client = gmusicapi.Mobileclient()
    client.login(username, password, gmusicapi.Mobileclient.FROM_MAC_ADDRESS)

    playlists = []
    generated_songs = client.get_all_songs()
    generated_playlists = client.get_all_user_playlist_contents()
    for generated_playlist in generated_playlists:
        playlist = Playlist(generated_playlist["name"])
        for generated_track_container in generated_playlist["tracks"]:
            identifier = generated_track_container["trackId"]
            if "track" in generated_track_container:
                generated_track = generated_track_container["track"]
                playlist.songs.append(Song(
                    generated_track["title"],
                    generated_track["artist"],
                    generated_track["album"],
                    identifier))
            else:
                for generated_song in generated_songs:
                    if generated_song["id"] == identifier:
                        playlist.songs.append(Song(
                            generated_song["title"],
                            generated_song["artist"],
                            generated_song["album"],
                            identifier))
                        break
                else:
                    raise LookupError("Couldn't find ID in song list.")

        playlists.append(playlist)

    client.logout()
    return playlists
