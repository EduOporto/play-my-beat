# Build a function to get the last workouts (up to last 10) in sql_db_functions 
#from model.concat_last.min_registers import first_of_minute
from forecast.arima_model.grid_search import *
from forecast.arima_model.model import *

def prediction():
    # Build a function to get the last workouts (up to last 10) in sql_db_functions 
    # last_workouts = call the function

    minreg_df = first_of_minute(last_ten).to_period('min')
    rows_n = minreg_df['1970-01-01'].shape[0]
    
    order, seasonal_order = (1, 1, 1), (0, 1, 1, rows_n) #grid_search(minreg_df)

    get_prediction(minreg_df, order, seasonal_order)