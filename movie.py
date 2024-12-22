class Movie:
    def __init__(self, title, director, genre, release_year):
        self.title = title
        self.director = director
        self.genre = genre
        self.release_year = release_year

    def __repr__(self):
        return f"Movie({self.title}, {self.director}, {self.genre}, {self.release_year})"
