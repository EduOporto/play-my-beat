import pandas as pd
import time

def playlist_data(oauth, playlist_uri):
    
    # Get list of playlist's songs
    playlist_tracks_uris = oauth.playlist_tracks(playlist_uri)

    playlist_songs = [e['track']['uri'] for e in playlist_tracks_uris['items']]
    playlist_lengths = [e['track']['duration_ms'] / 1000 for e in playlist_tracks_uris['items']]
    playlist_tempos = [e['tempo'] for e in oauth.audio_features(playlist_songs)]
    
    # Get lenght and tempo of the songs, and join all in a dataframe
    playlist_dict = {'uri': playlist_songs, 
                     'length': playlist_lengths, 
                     'tempo': playlist_tempos}
    
    playlist_df = pd.DataFrame(playlist_dict)
    playlist_mean = round(playlist_df.length.mean() / 60)

    return playlist_df, playlist_mean    