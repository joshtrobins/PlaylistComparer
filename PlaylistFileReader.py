import csv
from Song import Song
from Playlist import Playlist


def read(path):
    with open(path, "r", encoding="utf-8", newline="") as file:
        playlists = []
        row_count = 0
        for row in csv.reader(file):
            if row_count == 0:
                title_index = row.index("title")
                artist_index = row.index("artist")
                album_index = row.index("album")
                id_index = row.index("id")
                playlist_index = row.index("playlist")
            else:
                song = Song(row[title_index], row[artist_index], row[album_index], row[id_index])
                playlist_name = row[playlist_index]

                for playlist in playlists:
                    if playlist.name == playlist_name:
                        matching_playlist = playlist
                        break
                else:
                    matching_playlist = Playlist(playlist_name)
                    playlists.append(matching_playlist)

                matching_playlist.songs.append(song)

            row_count += 1

    return playlists
