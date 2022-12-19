class Music :
    def __init__(self, artist,track,title,album,year):
        self.artist = artist
        self.track = track
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return "Performer: " + self.artist +"\nSong: " + self.track + "\nAlbum: " + self.album + '\nYear: ' + self.year



Music1 = Music('Ed Sheeran' , "hearts Don't Break Around Here" , 'some' , 'Divide','2017')

print(Music1)
print()
Music2 = Music("Łajcior2115",'18','18','afterparty','2022')
print(Music2)