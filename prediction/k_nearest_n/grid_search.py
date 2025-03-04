from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np

def grid_search(X, y, max_min_predict):

    # Set range of parameters
    parameters = {'weights': ['uniform', 'distance'],
              'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
              'leaf_size': np.arange(10,70,10)}

    # Grid Search and model fitting
    kNeigh = KNeighborsRegressor(n_neighbors=4)

    grid_kNeigh = GridSearchCV(kNeigh, parameters)
    grid_kNeigh.fit(X, y)

    # Make next workout prediction
    minutes = np.arange(1, max_min_predict)
    bpm_prediction = grid_kNeigh.predict(minutes.reshape(-1, 1)).round().flatten() 

    # Create a dataframe with the predictions
    prediction = pd.DataFrame({'min': minutes, 'bpm': bpm_prediction})

    return prediction
