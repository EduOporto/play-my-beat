import numpy as np
import datetime
import pandas as pd

def day_assign(dframe):

    # Detect the different runs for which there are registers (through id) and sort the list ascending
    diff_runs = dframe.run_id.value_counts().index.sort_values()
    # Make a list from 0 to number of different runs - 1, in order to assign each of the runs a number of days
    # This way, each of the runs will be differenciated, and build a model will be possible
    days_sum = np.arange(len(diff_runs))
    
    # Join the latter lists into a dict, where the run ids are the keys and the number of days assigned to that
    # run will be the values
    f_dict = dict(zip(diff_runs, days_sum))
    
    # Map the dict to the id column
    dframe.run_id = dframe.run_id.map(f_dict)
    # Convert the int number assigned to a timedelta object
    dframe.run_id = dframe.run_id.apply(lambda x: datetime.timedelta(days=x))
    
    # Sum the modified ids column to run_min, so each of the bpm registred will have a date of register
    dframe.run_min = dframe.run_id + dframe.run_min

    # Set run_min as index and drop it as a column
    dframe = dframe[['run_min', 'bpm']]
    dframe.sort_values(['run_min'], inplace=True)
    dframe.index = pd.to_datetime(dframe.run_min.astype(np.int64))
    dframe.drop(['run_min'], axis=1, inplace=True)
    
    return dframe