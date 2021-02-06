
def heart_data_uploader(sql_conn, dframe, id_):
    # Iterate through the BPM registers, adding every register time and data to the database
    for index, row in dframe.iterrows():
        minute = row.acc_time.to_pytimedelta()
        data = row.bpm
        
        insert_query = f"""INSERT INTO play_my_beat.heart_rate (run_id, run_min, bpm)
                            VALUES ('{id_}', '{minute}', '{data}')"""
        
        sql_conn.execute(insert_query)
    
    return f"Heart data for workout {id_} succesfully added to the database"

def misc_data_uploader(sql_conn, data, id_):

    insert_query = f"""INSERT INTO play_my_beat.other_data (run_id, distance, steps, calories)
                            VALUES ('{id_}', '{data[0]}', '{data[1]}', '{data[2]}')"""

    sql_conn.execute(insert_query)

    return f"Distance, steps and calories for workout {id_} succesfully added to the database"

def prediction_uploader(sql_conn, dframe, pred_date):
    # Delete last prediction
    delete_query = """DELETE FROM play_my_beat.last_prediction"""
    sql_conn.execute(delete_query)

    # Iterate through the BPM predictions, adding every register time and data to the database
    for index, row in dframe.iterrows():
        minute = row['min']
        data = int(row['bpm'])
        
        insert_query = f"""INSERT INTO play_my_beat.last_prediction (pred_date, pred_min, pred_bpm)
                            VALUES ('{pred_date}', '{minute}', '{data}')"""
        
        sql_conn.execute(insert_query)

    return f"Heart prediction for your workout on {pred_date} succesfully added to the database"