from sql_db.update_db.update_db import *
from spotify_api.pl_builder.get_playlist import *

def update_db():
    new_sessions = session_update(30)

    if len(new_sessions) > 0:
        for session_id in new_sessions:
            hrates = heart_rate_update(session_id)
            if hrates != None:
                misc_data_update(hrates)

# Call to create a playlist sorted according to the predicted heart rate behaviour
# get_playlist(playlist_uri, prediction)

