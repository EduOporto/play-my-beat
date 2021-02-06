import datetime

def playlist_generator(oauth, user, songs_uri_sorted):
    
    # Create the playlist on the user's profile, with the actual date as name
    year, month, day = datetime.date.today().year, datetime.date.today().month, datetime.date.today().day
    playlist_id = oauth.user_playlist_create(user, name=f'Playlist for workout {year}-{month}-{day}')['id']
    # ADD A PICTURE FOR THE NEW PLAYLIST

    # Fill the playlist with the songs in the selected order
    oauth.user_playlist_add_tracks(user, playlist_id, songs_uri_sorted)

    print(f"""
        \nPlaylist succesfully generated in your library, 
    search for it as 'Playlist for workout {year}-{month}-{day}' 
    
    ENJOY YOUR WORKOUT!""")