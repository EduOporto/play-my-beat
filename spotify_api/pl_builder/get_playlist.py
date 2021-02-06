from spotify_api.service.spoti_service import *
from spotify_api.playlist_functions.pl_data import *
from spotify_api.playlist_functions.pl_sorter import *
from spotify_api.playlist_functions.pl_generator import *
import time

import pandas as pd
pd.options.mode.chained_assignment = None 

user, oauth = get_oauth()

def get_playlist(playlist_uri, prediction):

    # Get a dataframe of the songs' lenght and tempo in a given playlist 
    playlist_df, playlist_mean = playlist_data(oauth, playlist_uri)
    
    # Through the mean length of the playlist in rounded minutes, get an stimation of what the heart BPM
    # will be in the intervals between a song finishes and a new one starts 
    run_intervals = prediction[prediction.pred_min % playlist_mean == 0]
    
    # SONG SORTAGE
    # This function takes the predicted run with just the values for the intervals of the playlist and 
    # returns a list with the sorted songs
    songs_sorted = playlist_sorter(run_intervals, playlist_df)
    
    # Create the playlist on the user's profile, with the actual date as name; and fill it with the list of 
    # sorted songs
    playlist_generator(oauth, user, songs_sorted)