
def heart_data_uploader(sql_conn, dframe, id_):
    # Iterate through the BPM registers, adding every register time and data to the database
    for index, row in dframe.iterrows():
        minute = row.acc_time.to_pytimedelta()
        data = row.bpm
        
        insert_query = f"""INSERT INTO play_my_beat.heart_rate (run_id, run_min, bpm)
                            VALUES ('{id_}', '{minute}', '{data}')"""
        
        sql_conn.execute(insert_query)
    
    print(f"\nHeart data for workout {id_} succesfully added to the database")

def misc_data_uploader(sql_conn, data, id_):

    insert_query = f"""INSERT INTO play_my_beat.other_data (run_id, distance, steps, calories)
                            VALUES ('{id_}', '{data[0]}', '{data[1]}', '{data[2]}')"""

    sql_conn.execute(insert_query)

    print(f"\nDistance, steps and calories for workout {id_} succesfully added to the database")