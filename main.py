from sql_db.update_db.update_db import *
from spotify_api.pl_builder.get_playlist import *
from forecast.k_nearest_n.get_prediction import *

# Call to check if there are new workouts yet not uploaded to the databases
# It takes the days to check for workouts as input
# update_db(31)

# Call to get a prediction of the last workouts
# prediction = get_prediction()

# Call to create a playlist sorted according to the predicted heart rate behaviour
# get_playlist(playlist_uri, prediction)