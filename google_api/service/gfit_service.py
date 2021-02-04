import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
 
def flow_cred():
    client_secret_file = 'google_api/service/client_secrets.json'
    
    scopes = ['https://www.googleapis.com/auth/fitness.heart_rate.read',
              'https://www.googleapis.com/auth/fitness.heart_rate.write', 
              'https://www.googleapis.com/auth/fitness.activity.read',
              'https://www.googleapis.com/auth/fitness.activity.write',
              'https://www.googleapis.com/auth/fitness.body.read',
              'https://www.googleapis.com/auth/fitness.body.write',
              'https://www.googleapis.com/auth/fitness.location.read',
              'https://www.googleapis.com/auth/fitness.sleep.read',
              'https://www.googleapis.com/auth/fitness.sleep.write']

    flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
    cred = flow.run_local_server()

    return cred

def create_fit_service():
    cred = None
 
    pickle_file = f'token_fitness_v1.pickle'
 
    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)        
    
    if not cred or not cred.valid:
        if cred and cred.refresh_token and cred.expired:
            try:
                cred.refresh(Request())
            except:
                os.remove(pickle_file)
                cred = flow_cred()
        else:
            cred = flow_cred()
 
        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)
 
    try:
        service = build('fitness', 'v1', credentials=cred)
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None