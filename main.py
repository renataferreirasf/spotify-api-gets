from spotify import TSpotify
import json


def start():
    spotify = TSpotify("", "")
    token = spotify.getAccessToken()

    artist = spotify.getArtist(token, "7FNnA9vBm6EKceENgCGRMb?si=HAeEfRxvTMq_Dh1iGhEuRw")
    with open('artist.json', 'w') as f:
        json.dump(artist, f)

    playlist = spotify.getPlayList(token, "0PCZ02z75sz7cZONJt1gPT?si=a1c5990814aa4a8c")
    with open('playlist.json', 'w') as f:
        json.dump(playlist, f)

    tracks = spotify.getTracks(token, "1hy6Dic0L5SU1XqjhYY1TR?si=d65e71f91ca54f32")
    with open('tracks.json', 'w') as f:
        json.dump(tracks, f)

if __name__ == "__main__":
    start()


