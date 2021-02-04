from google_api.service.gfit_service import *
from sql_db.sql_engine_conector.sql_engine_conector import *
from google_api.get_sessions.get_sessions import *
from sql_db.sql_db_functions.workout_uploader.workout_uploader import workout_uploader
from sql_db.sql_db_functions.workout_dates.workout_dates import *
from google_api.get_data.get_data import get_data
from sql_db.sql_db_functions.data_uploader.data_uploader import *

# Start Google Fit API service
gfit_service = create_fit_service()

# Start SQLAlchemy service
sql_conn = engine_connector()

def session_update(days):

    # Get sessions registred on the API as Dataframe
    mi_fit_running = get_sessions(gfit_service, 'Running', days)

    # Get workouts registred on the database
    query = f"""SELECT * FROM play_my_beat.runs"""

    registred_runs = pd.read_sql(sql=query, con=sql_conn)
    registred_runs

    # Check if the workouts registred on Google Fit have been already saved on the DB
    # If not, this function will upload the workout and return a list with the IDs of 
    # each of the new uploaded workouts
    new_wkouts_id = workout_uploader(mi_fit_running, registred_runs, sql_conn)

    return new_wkouts_id

def heart_rate_update(id_):
    # Getting start and end dates of the given workout
    start_date, end_date = workout_dates(sql_conn, id_)

    # Getting a dataframe with the heart rates of the given workout
    # dataSourceId = 'raw:com.google.heart_rate.bpm:com.xiaomi.hm.health:'
    dataSourceId = 'derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm'
    hr_df = get_data(gfit_service, dataSourceId, start_date, end_date)

    # Upload data to the databases: if there is any heart rate data to upload, save the id of the workout, 
    # in order to get also the miscellaneous data

    if hr_df.shape[0] >= 20:
        heart_data_uploader(sql_conn, hr_df, id_)
        
        return id_

    else:
        return None

def misc_data_update(id_):
    # Getting start and end dates of the given workout
    start_date, end_date = workout_dates(sql_conn, id_)

    # Getting the values for steps, distance, and calories of a given workout id
    distance = get_data(gfit_service, 'derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta', start_date, end_date)
    steps = get_data(gfit_service, 'derived:com.google.step_count.delta:com.google.android.gms:merge_step_deltas', start_date, end_date)
    calories = get_data(gfit_service, 'derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended', start_date, end_date)

    data = [distance, steps, calories]

    # Upload to the databases
    misc_data_uploader(sql_conn, data, id_)

    
def update_db(days_to_check):
    # Check for new sessions, if there is any the function will return a list with the IDs of the workouts 
    # uploaded; otherwise return an empy list
    new_sessions = session_update(days_to_check)

    # Check if there are new workouts uploaded
    if len(new_sessions) > 0:
        # If so, iterate through the IDs
        for session_id in new_sessions:
            # Update the heart rates of each of the workouts
            hrates = heart_rate_update(session_id)
            # Update the rest of the data
            if hrates != None:
                misc_data_update(hrates)
    

    


    




