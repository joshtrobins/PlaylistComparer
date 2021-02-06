import os.path

import PlaylistComparer
import PlaylistFileReader
import PlaylistFileWriter
import PlaylistScraper

full_path = input("Path: ").strip("\"")
path, file = os.path.split(full_path)
config_path = path + "\\config.txt"

client_id = ""
client_secret = ""
username = ""
if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8", newline="") as config_file:
        lines = config_file.readlines()
        for line in lines:
            if line.startswith("Client ID:"):
                client_id = line[10:].strip()
            elif line.startswith("Client Secret:"):
                client_secret = line[14:].strip()
            elif line.startswith("Username:"):
                username = line[9:].strip()
else:
    client_id = input("Client ID: ")
    client_secret = input("Client Secret: ")
    username = input("Username: ")

new_playlists = PlaylistScraper.scrape(client_id, client_secret, username)
old_playlists = PlaylistFileReader.read(full_path)
PlaylistFileWriter.write(path, new_playlists)
PlaylistComparer.compare(path, old_playlists, new_playlists)
