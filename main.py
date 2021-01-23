from sql_db.update_db.update_db import *

new_sessions = session_update(30)

if len(new_sessions) > 0:
    for session_id in new_sessions:
        heart_rate_update(session_id)
        misc_data_update(session_id)
else:
    pass