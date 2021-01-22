
def heart_data_uploader(sql_conn, dframe, id_):
    # Iterate through the BPM registers, adding every register time and data to the database
    for index, row in dframe.iterrows():
        minute = row.acc_time.to_pytimedelta()
        data = row.bpm
        
        insert_query = f"""INSERT INTO play_my_beat.heart_rate (runs_run_id, run_min, bpm)
                            VALUES ('{id_}', '{minute}', '{data}')"""
        
        
        sql_conn.execute(insert_query)
    
    print(f"\nData for workout {id_} succesfully added to the database")

#def misc_data_uploader():