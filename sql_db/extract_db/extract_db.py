from sql_db.sql_engine_conector.sql_engine_conector import *
import pandas as pd
from sql_db.sql_db_functions.day_assign.day_assign import *

# Start SQLAlchemy service
sql_conn = engine_connector()

def heart_rate_extract():
    # Get the heart rates as dataframe
    query = """SELECT run_id, run_min, bpm FROM play_my_beat.heart_rate"""
    heart_rates = pd.read_sql(sql=query, con=sql_conn)

    # Sort by run_id
    heart_rates.sort_values(['run_id'], inplace=True)

    # If there are more than 10 workouts registred, select the last 10; otherwise, get all
    n_workouts = heart_rates.run_id.value_counts().index.sort_values()

    if len(n_workouts) > 10:
        heart_rates = heart_rates[heart_rates.run_id.isin(n_workouts[-10:])]
    else:
        pass

    # Get the minimum number of registers available
    min_regs = min(heart_rates.run_id.value_counts().to_list())

    # Modify the run_min column, so each of the runs have different timedelta days 
    heart_rates_day = day_assign(heart_rates)

    return heart_rates_day, min_regs

