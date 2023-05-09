import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.raaga.com/tamil/album/ilayaraja-top-100-songs-TC0001726"
CLIENT_ID = ""
CLIENT_SECRET = ""

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

songs_list = soup.find_all(name="a", itemprop="name")
songs_name = [song_name.getText() for song_name in songs_list]

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

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
