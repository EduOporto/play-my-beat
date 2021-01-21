import datetime
import pytz

## This function returns the date when the request is done and the date x days ago since the request is done
## Right now is set for 60 days by default, could be a future improvement for this to be passes as an argument

def days_ago_now():
    # Get the actual date of the request
    d = datetime.datetime.utcnow()
    d_with_timezone = d.replace(tzinfo=pytz.UTC)
    now = d_with_timezone.isoformat()

    # Get the date from which the user wants to list the activities
    date_days_ago = (d_with_timezone - datetime.timedelta(days = 60)).isoformat() # I fix 60 days by default, but this could be passed as an argument in the future

    return date_days_ago, now