from google_api.google_api_functions.days_ago_now.days_ago_now import *
from google_api.google_api_functions.date_format.date_format import *
from google_api.google_api_functions.activityTypes.activityTypes_df import *
import pandas as pd

def get_sessions(service, activityType):
    
    # DATES using function 'days_ago_now' 
    date_days_ago, now = days_ago_now()

    sess_req = service.users().sessions().list(userId='me',
                                                startTime=date_days_ago, 
                                                endTime=now,
                                                includeDeleted=False).execute()['session']

    sessions_df = pd.DataFrame({'activityType': [types_df(e['activityType']) for e in sess_req], 
                                'startDate': [mill_to_date(int(e['startTimeMillis'])) for e in sess_req],                                
                                'endDate': [mill_to_date(int(e['endTimeMillis'])) for e in sess_req],                                
                                'packName': [e['application']['packageName'] for e in sess_req]})

    # Get all the sessions which activityType is Running and have been registred by the Mi Fit APP
    req_sessions = sessions_df[(sessions_df.activityType == activityType) &
                                (sessions_df.packName == 'com.xiaomi.hm.health')].sort_values('startDate').reset_index(drop=True)

    return req_sessions

    