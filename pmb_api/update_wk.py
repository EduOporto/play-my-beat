from sql_db.update_db.update_db import *

def update_wk(st):    
    # Check for new sessions, if there is any the function will return a list with the IDs of the workouts 
    # uploaded; otherwise return an empy list
    days_to_check = st.slider('How many days ago would you like to check?', 1, 80, 14)

    new_sessions, upd_message = session_update(days_to_check)
    st.success(upd_message)

    # Check if there are new workouts uploaded
    if len(new_sessions) > 0:
        # If so, iterate through the IDs
        for session_id in new_sessions:
            # Update the heart rates of each of the workouts

            hrates, hr_message = heart_rate_update(session_id)
            st.success(hr_message)

            # Update the rest of the data
            if hrates != None:
                misc_message = misc_data_update(hrates)
                st.success(misc_message)
