"""
✨ Here at Codédex, we are 🤩 big fans of music 🎹. The only thing better than a perfect playlist is a playlist with all your favorite songs. Let's create a Python script that organizes the songs into a .txt file. Let's make a playlist!

First, let's define a dictionary to store liked songs:

liked_songs = {
  'title': 'artist'
}

Next, create a function to display and write liked songs to a file:

def write_liked_songs_to_file(liked_songs, file_name):

Open the file in write mode.
Write each song and artist by iterating through the liked_songs dictionary.
"""

liked_songs = {
    'Blinding Lights': 'The Weeknd',
    'As It Was': 'Harry Styles',
    'Levitating': 'Dua Lipa'
}

def write_liked_songs_to_file(songs_like, file_name):
    with open(file_name, "w") as f:
        f.write("My favorite songs\n")
        for songs, artist in songs_like.items():
            f.write(f"Song: {songs}, Artist: {songs}\n")

write_liked_songs_to_file(liked_songs, "file.txt")