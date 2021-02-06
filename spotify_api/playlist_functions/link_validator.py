from spotify_api.service.spoti_service import *

user, oauth = get_oauth()

def link_validator(pl_uri):

    try:
        oauth.playlist(pl_uri)
        valid = 'Yes'
    except:
        valid = 'No'

    return valid