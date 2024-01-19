import csv
import pandas as pd


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

    @staticmethod
    def create_playlist(playlist):

        with open("DataSample.csv", "r") as file:
            reader = pd.read_csv(file)

        if playlist not in reader:
            reader[playlist] = ""
            reader.to_csv("DataSample.csv", index=False)
            print("Playlist created")
        else:
            print("Playlist is existing")

    @staticmethod
    def add_song(title, playlist):
        with (open("DataSample.csv", "r") as file):
            df = pd.read_csv(file)

            if title not in df["Title"].values or playlist not in df.columns:
                print("Music or playlist not found")

            elif title in df[playlist].values:
                print("Music is already in the playlist")

            elif title in df["Title"].values and playlist in df.columns:
                first_empty_cell = df[playlist].isnull().idxmax()
                df.loc[first_empty_cell, [playlist]] = [title]
                df.to_csv("DataSample.csv", index=False)
                print(title, "added to", playlist)

    @staticmethod
    def remove_song(title, playlist):
        with open("DataSample.csv", "r") as file:
            df = pd.read_csv(file)

        if title not in df["Title"].values or playlist not in df.columns:
            print("Music or playlist not found")

        elif title in df["Title"].values and playlist in df.columns:
            df.drop(df[df[playlist] == title].index, inplace=True)
            df.to_csv("DataSample.csv", index=False)
            print(title, "removed from", playlist)

    @staticmethod
    def Shuffle(playlist):
        with open("DataSample.csv", "r") as file:
            df = pd.read_csv(file)

            if playlist not in df.columns:
                print("Playlist not found")
            elif playlist in df.columns:
                df = df[playlist]
                df.to_csv("DataSample.csv", index=False)
                print("Playlist shuffled")

    @staticmethod
    def display_playlist(playlist):
        with open("DataSample.csv", "r") as file:
            df = pd.read_csv(file)
        if playlist in df.columns:
            print("Your playlist: \n", df[playlist])
        else:
            print("Playlist not found")

