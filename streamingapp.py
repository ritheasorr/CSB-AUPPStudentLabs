import csv


class Song:

    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length


class MusicLibrary:
    def __init__(self):
        self.song = {}

    @staticmethod
    def get_songs_by_artist(artist):
        with open("DataSample.csv", "r") as file:
            reader = csv.DictReader(file)
            artist_data = [row for row in reader]

        if any(row["Artist"] == artist for row in artist_data):
            print("Here are the musics by", artist)
            for row in artist_data:
                if row["Artist"] == artist:
                    print('-', row["Title"])
            return artist_data
        else:
            print("Artist not found")

    def get_songs_by_album(album):
        with open("DataSample.csv", "r") as file:
            reader = csv.DictReader(file)
            album_data = [row for row in reader]

            if any(row["Album"] == album for row in album_data):
                print("Here are the musics in", album)
                for row in album_data:
                    if row["Album"] == album:
                        print('-', row["Title"])
                return album_data
            else:
                print("album not found")

    @staticmethod
    def get_songs_by_genre(genre):
        with open("DataSample.csv", "r") as file:
            reader = csv.DictReader(file)
            genre_data = [row for row in reader]

            if any(row["Genre"] == genre for row in genre_data):
                print("Here are the musics in", genre)
                for row in genre_data:
                    if row["Genre"] == genre:
                        print('-', row["Title"])
                return genre_data
            else:
                print("Genre not found")

    @staticmethod
    def get_songs_by_title(title):
        with open("DataSample.csv", "r") as file:
            reader = csv.DictReader(file)
            title_data = [row for row in reader]

        if any(row["Title"] == title for row in title_data):
            print(title, "by")
            for row in title_data:
                if row["Title"] == title:
                    print('-', row["Artist"], '-', row["Album"], '-', row["Genre"], '-', row["Length"])
            return title_data
        else:
            print("Title not found")

#
#
class Playlist:
    def __init__(self):
        self.playlist = []

    @staticmethod
    def add_song(title):

        with open("DataSample.csv", "r") as file:
            read = csv.reader(file)
            rows = [row for row in read]

        with open("DataSample.csv", "w") as file:
            type(file)
            writer = csv.writer(file)
            writer.writeheader()
            writer.writerow(title)
#
#     def remove_song(self, song):
#
#     def reorder_songs(self, new_order):
#
#     def display_playlist(self):
