import datetime
import numpy as np
from decimal import Decimal

def date_to_mill(year, month, day, hour, mit):
    epoch = datetime.datetime.utcfromtimestamp(0)

    date = datetime.datetime(year, month, day, hour, mit)

    return Decimal((date - epoch).total_seconds() * 1000)

def date_to_nano(year, month, day, hour, mit):
    epoch = datetime.datetime.utcfromtimestamp(0)

    date = datetime.datetime(year, month, day, hour, mit)

    return Decimal((date - epoch).total_seconds() * 1000000000)

def mill_to_date(mill):
    return datetime.datetime.fromtimestamp(mill/1000)

def nano_to_date(nano):
    return datetime.datetime.fromtimestamp(nano/1000000000)

def mill_to_nano(mill):
    return mill * 1000000

def date_to_periods(acc_series):

    stops = np.arange(1,acc_series.shape[0])
    starts = np.arange(acc_series.shape[0]-1)

    progress = [datetime.timedelta(0)]
    for stop, start in zip(stops, starts):
        difference = acc_series[stop] - acc_series[start]
        progress.append(progress[-1] + difference)

    return progress
