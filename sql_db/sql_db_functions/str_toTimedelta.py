import datetime

def str_toTimedelta(time_str):
    time = datetime.datetime.strptime(time_str, '%H:%M:%S')
    t_delta = datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)
    
    return t_delta