class Song:
    """Class to represent a song

    Attributes:
    
        title (str): THe title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero
    """"

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

print(Song.__doc__)
print(Song.__init.__doc__ )
