import os.path
import PlaylistComparer
import PlaylistFileReader
import PlaylistFileWriter
import PlaylistScraper

full_path = input("Path: ").strip("\"")
path, file = os.path.split(full_path)

process_library = input("Library: ") in ('true', '1', 't', 'y', 'yes')

username = input("Username: ")
password = input("Password: ")

old_playlists = PlaylistFileReader.read(full_path)
new_playlists = PlaylistScraper.scrape(username, password, process_library)
PlaylistFileWriter.write(path, new_playlists)
PlaylistComparer.compare(path, old_playlists, new_playlists)
