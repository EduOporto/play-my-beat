import pandas as pd

def playlist_data(oauth, playlist_uri):
    # Get list of playlist's songs
    playlist_songs = [e['track']['uri'] for e in oauth.playlist_tracks(playlist_uri)['items']]

    # Get lenght and tempo of the songs, and join all in a dataframe
    playlist_dict = {'uri': playlist_songs, 'length': [], 'tempo': []}
    
    for song in playlist_songs:
        analysis = oauth.audio_analysis(song)
        playlist_dict['length'].append(analysis['track']['duration'])
        playlist_dict['tempo'].append(analysis['track']['tempo'])
    
    playlist_df = pd.DataFrame(playlist_dict)
    playlist_mean = round(playlist_df.length.mean() / 60)

    return playlist_df, playlist_mean