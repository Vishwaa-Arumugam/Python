import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# year = input("Which year do you want to? Type the date in this format YYYY-MM-DD : ")


URL = "https://www.raaga.com/tamil/album/ilayaraja-top-100-songs-TC0001726"
CLIENT_ID = "1f2baa7b49ae4064beb1c0885f2b77f0"
CLIENT_SECRET = "5717f702a32b4444b79ca1a229631838"

response = requests.get(URL)
website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")

songs_list = soup.find_all(name="a", itemprop="name")
songs_name = [song_name.getText() for song_name in songs_list]
# print(songs_name)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# print(user_id)

song_uris = []
for song in songs_name:
    result = sp.search(q=f"track:{song}"
                         , type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=f"{user_id}", name=f"ilayaraja hits",
                                   public=False, description="Enjoy❤")

print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
