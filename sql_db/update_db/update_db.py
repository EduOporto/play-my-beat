# Google Fit API libraries
from google_api.service.gfit_service import *
from google_api.get_sessions.get_sessions import *
from google_api.get_data.get_data import get_data

# SQL Database libraries
from sql_db.sql_engine_conector.sql_engine_conector import *
from sql_db.sql_db_functions.workout_uploader import workout_uploader
from sql_db.sql_db_functions.workout_dates import *
from sql_db.sql_db_functions.data_uploader import *

# Forecast libraries
from prediction.k_nearest_n.get_prediction import get_prediction

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
    new_wkouts_id, message = workout_uploader(mi_fit_running, registred_runs, sql_conn)

    return new_wkouts_id, message

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
        message = heart_data_uploader(sql_conn, hr_df, id_)
        
        return id_, message

    else:
        return None, 'Not enough data to update'

def misc_data_update(id_):
    # Getting start and end dates of the given workout
    start_date, end_date = workout_dates(sql_conn, id_)

    # Getting the values for steps, distance, and calories of a given workout id
    distance = get_data(gfit_service, 'derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta', start_date, end_date)
    steps = get_data(gfit_service, 'derived:com.google.step_count.delta:com.google.android.gms:merge_step_deltas', start_date, end_date)
    calories = get_data(gfit_service, 'derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended', start_date, end_date)

    data = [distance, steps, calories]

    # Upload to the databases
    message = misc_data_uploader(sql_conn, data, id_)

    return message
    
def prediction_update():
    # Get a prediction
    prediction = get_prediction()

    # Get the actual date
    actual_date = datetime.datetime.today().strftime('%Y-%m-%d')

    # Upload to the databases
    message = prediction_uploader(sql_conn, prediction, actual_date)

    return prediction, message
    




