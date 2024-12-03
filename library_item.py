class LibraryItem:
    #initializer method for the class.
    def __init__(self, name, artist, rating=0, play_count=0):
        self.name = name
        self.artist = artist
        self.rating = rating
        self.play_count = 0
    #method returns a formatted string containing details about the library item.
    def info(self):
        return f"{self.name} - {self.artist} {self.stars()}"
    #generates a string of asterisks (*) corresponding to the rating of the track.
    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars


