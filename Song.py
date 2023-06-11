class Song:
    title = ""
    artist = ""
    album = ""
    identifier = ""
    playable = False
    local = False

    def __init__(self, title, artist, album, identifier, playable, local):
        self.title = title
        self.artist = artist
        self.album = album
        self.identifier = identifier
        self.playable = playable
        self.local = local
