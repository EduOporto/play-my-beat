from google_api.google_api_functions.date_format import *
import pandas as pd

def get_data(gfit_service, dataSourceId, startDate, endDate):
    # Google Fit API call
    dataset = gfit_service.users().dataSources().datasets().get(userId='me',
                                                                dataSourceId = dataSourceId,
                                                                datasetId=f"{str(startDate)}-{str(endDate)}").execute()

    if 'heart_rate' in dataSourceId:
        # nanoseconds epoch to date format)
        dates = [nano_to_date(int(e['startTimeNanos'])) for e in dataset['point']]

        # List of the BPM registered
        bpm = [e['value'][0]['fpVal'] for e in dataset['point']]

        # Build the dataframe, convert the dates to periods and get the round minute of each of the measures
        df = pd.DataFrame({'acc_time': dates, 'bpm': bpm})
        df['acc_time'] = date_to_periods(df['acc_time'])
        df['acc_time'] = df.acc_time.apply(lambda x: x.round('min'))

        # Get data just from each of the minutes
        df.drop_duplicates(subset=['acc_time'], inplace=True)

        return df
    
    elif 'step_count' in dataSourceId:
        return dataset['point'][0]['value'][0]['intVal']

    else:
        return dataset['point'][0]['value'][0]['fpVal']

