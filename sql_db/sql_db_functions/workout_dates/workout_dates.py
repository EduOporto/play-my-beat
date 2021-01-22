from google_api.google_api_functions.date_format.date_format import *
import pandas as pd

def workout_dates(sql_conn, id_):
    # SQL query for getting start and end dates of the given workout
    session_query = f"""SELECT * FROM play_my_beat.runs
                        WHERE run_id = {id_}"""
    exc_query = pd.read_sql(sql=session_query, con=sql_conn)
    
    start_date = exc_query.start_date[0]
    end_date = exc_query.end_date[0]

    # Transform dates to nano, in order to make the query on Google Fit API
    start_date_nano = date_to_nano(start_date.year, start_date.month, start_date.day, start_date.hour, start_date.minute)
    end_date_nano = date_to_nano(end_date.year, end_date.month, end_date.day, end_date.hour, end_date.minute)

    return start_date_nano, end_date_nano