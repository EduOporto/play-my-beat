
def workout_uploader(gfit_workouts, db_workouts, sql_conn):    
    # List of workouts already on the DB
    reg_runs_start = db_workouts.start_date.to_list()
    
    # Number of workouts uploaded during the process
    runs_to_db = 0

    # Dates of updated workouts
    updated_wkouts = []

    for index, row in gfit_workouts.iterrows():
        if row['startDate'] in reg_runs_start:
            pass
        else:
            runs_to_db += 1
            
            start_date = row['startDate'].to_pydatetime()
            start_date_nano = row['startDate_nano']
            
            end_date = row['endDate'].to_pydatetime()
            end_date_nano = row['endDate_nano']

            # Insert the workout on the DB
            insert_query = f"""INSERT INTO play_my_beat.runs(start_date, start_date_nano, end_date, end_date_nano)
                            VALUES ('{start_date}', '{start_date_nano}', '{end_date}', '{end_date_nano}')"""
            
            sql_conn.execute(insert_query)

            # Get the id of the workout inserted
            id_query = f"""SELECT run_id FROM play_my_beat.runs
                            ORDER BY run_id DESC
                            LIMIT 1"""
        
            result = sql_conn.execute(id_query)
            id_ = [id_[0] for id_ in result][0]

            # Save the id of the updated workout
            updated_wkouts.append(id_)

    if runs_to_db == 0:
        print('\nThere was no new workouts to be added to the database')
    elif runs_to_db == 1:
        print('\nA new workout has been added to the database')
    else:
        print(f'\n{runs_to_db} new workouts have been added to the database')

    return updated_wkouts
