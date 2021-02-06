from sql_db.sql_engine_conector.sql_engine_conector import *
import pandas as pd

# Start SQLAlchemy service
sql_conn = engine_connector()

def heart_rate_extract():
    # Get the heart rates as dataframe
    query = """SELECT hr.run_id, CAST(r.start_date AS DATE) AS date, MINUTE(hr.run_min) AS min, hr.bpm 
                FROM play_my_beat.heart_rate AS hr 
                LEFT JOIN play_my_beat.runs AS r ON hr.run_id = r.run_id;
            """

    heart_rates = pd.read_sql(sql=query, con=sql_conn)

    # If there are more than 10 workouts registred, select the last 10; otherwise, get all
    n_workouts = heart_rates.run_id.value_counts().index.sort_values()

    if len(n_workouts) > 10:
        heart_rates = heart_rates[heart_rates.run_id.isin(n_workouts[-10:])]
    else:
        pass

    return heart_rates

def prediction_extract():
    # Get the current prediction
    query = """SELECT * FROM play_my_beat.last_prediction"""
    prediction = pd.read_sql(sql=query, con=sql_conn)
    
    # Get the date of the current prediction
    prediction_date = prediction.pred_date[0]

    return prediction, prediction_date

