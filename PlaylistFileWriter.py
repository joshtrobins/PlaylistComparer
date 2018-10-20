import csv
import datetime
import os.path


def write(path, playlists):
    path = os.path.join(path, "playlists_archive_" + datetime.date.today().strftime("%m%d%Y") + ".csv")
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "artist", "album", "id", "playlist"])
        for playlist in playlists:
            for song in playlist.songs:
                writer.writerow([song.title, song.artist, song.album, song.identifier, playlist.name])

    return
