from google_api.google_api_functions.service.gfit_service import *
from sql_db.sql_engine_conector.sql_engine_conector import *
from google_api.google_api_functions.get_sessions.get_sessions import *
from google_api.session_checker.workout_uploader.workout_uploader import workout_uploader
from google_api.google_api_functions.date_format.date_format import *

# Start Google Fit API service
gfit_service = create_fit_service()

# Start SQLAlchemy service
sql_conn = engine_connector()

def session_update():

    # Get sessions registred on the API as Dataframe
    mi_fit_running = get_sessions(gfit_service, 'Running')

    # Get workouts registred on the database
    query = f"""SELECT * FROM play_my_beat.runs"""

    registred_runs = pd.read_sql(sql=query, con=sql_conn)
    registred_runs

    # Check if the workouts registred on Google Fit have been already saved on the DB
    # If not, this function will upload the workout and return 
    new_wkouts_id = workout_uploader(mi_fit_running, registred_runs, sql_conn)

    return new_wkouts_id

#def heart_rate_update(id_):


