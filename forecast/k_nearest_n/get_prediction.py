from sql_db.extract_db.extract_db import *
from forecast.k_nearest_n.grid_search import grid_search

def get_prediction():

    # Get last registred workouts 
    runs = heart_rate_extract()

    # X & y
    X = runs[['min']]
    y = runs[['bpm']]

    # Get the highest minute of all the workouts, in order to predict the next workout's BPM 
    # until the very minute
    max_minute = X.max()['min']

    # Perform a grid search with the data available and return a prediction with the best parameters
    prediction = grid_search(X, y, 15, max_minute)

    return prediction
