from sql_db.extract_db.extract_db import *
from forecast.arima_model.grid_search import *
from forecast.arima_model.model import *

def get_prediction(grid_search=False):
    # Get the last workouts; if there are more than 10 registered, get the last 10, otherwise get them all
    # Get also the number of registers of the workout with less registers
    last_workouts, min_regiters = heart_rate_extract()

    if grid_search == True:
        # Perform a Grid Search, in order to tune the order and seasonal order parameters of the model
        order, seasonal_order = grid_search(last_workouts.to_period('min'), min_regiters)
    else:
        order, seasonal_order = (1, 1, 1), (0, 1, 1, min_regiters) 

    model(last_workouts, order, seasonal_order)