import spotipy
from spotipy.oauth2 import SpotifyOAuth

import os
from dotenv import load_dotenv
load_dotenv()

def get_oauth():
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
    user = os.getenv('USERNAME')

    scope = """user-library-read,
            app-remote-control, 
            user-modify-playback-state,  
            user-read-currently-playing, 
            streaming,
            playlist-modify-private, 
            playlist-modify-public,
            playlist-read-private,
            playlist-read-collaborative, 
            user-read-recently-played,
            user-library-read"""

    return user, spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))