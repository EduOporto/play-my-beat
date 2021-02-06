from google_api.google_api_functions.date_format import *
import pandas as pd

def workout_dates(sql_conn, id_):
    # SQL query for getting start and end dates of the given workout
    session_query = f"""SELECT * FROM play_my_beat.runs
                        WHERE run_id = {id_}"""
    exc_query = pd.read_sql(sql=session_query, con=sql_conn)
    
    # Get dates in nano, in order to make the query on Google Fit API
    start_date_nano = exc_query.start_date_nano[0]
    end_date_nano = exc_query.end_date_nano[0]

    return start_date_nano, end_date_nano