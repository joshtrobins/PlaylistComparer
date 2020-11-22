import os.path

import PlaylistComparer
import PlaylistFileReader
import PlaylistFileWriter
import PlaylistScraper

full_path = input("Path: ").strip("\"")
path, file = os.path.split(full_path)
client_id = input("Client ID: ")
client_secret = input("Client Secret: ")
username = input("Username: ")

new_playlists = PlaylistScraper.scrape(client_id, client_secret, username)
old_playlists = PlaylistFileReader.read(full_path)
PlaylistFileWriter.write(path, new_playlists)
PlaylistComparer.compare(path, old_playlists, new_playlists)
