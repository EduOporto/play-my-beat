from google_api.service.gfit_service import *
from sql_db.sql_db_functions.sql_engine_conector.sql_engine_conector import *
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
    # If not, this function will upload the workout and return 
    new_wkouts_id = workout_uploader(mi_fit_running, registred_runs, sql_conn)

    return new_wkouts_id

def heart_rate_update(id_):
    # Getting start and end dates of the given workout
    start_date, end_date = workout_dates(sql_conn, id_)

    # Getting a dataframe with the heart rates of the given workout
    dataSourceId = ['raw:com.google.heart_rate.bpm:com.xiaomi.hm.health:']
    hr_df = get_data(gfit_service, dataSourceId, start_date, end_date)

    # Upload data to the databases
    if hr_df.shape[0] >= 20:
        heart_data_uploader(sql_conn, hr_df, id_)

def misc_data_update(id_):
    # Getting start and end dates of the given workout
    start_date, end_date = workout_dates(sql_conn, id_)

    # Getting the values for steps, distance, and calories of a given workout id
    distance = get_data(gfit_service, 'raw:com.google.distance.delta:com.xiaomi.hm.health:', start_date, end_date)
    steps = get_data(gfit_service, 'raw:com.google.step_count.delta:com.xiaomi.hm.health:', start_date, end_date)
    calories = get_data(gfit_service, 'raw:com.google.calories.expended:com.xiaomi.hm.health:', start_date, end_date)

    data = [distance, steps, calories]

    # Upload to the databases
    misc_data_uploader(sql_conn, data, id_)

    

    

    


    




