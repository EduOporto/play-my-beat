from google_api.google_api_functions.date_format.date_format import nano_to_date, date_to_periods
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

        df = pd.DataFrame({'acc_time': dates, 'bpm': bpm})
        df['acc_time'] = date_to_periods(df['acc_time'])

        return df
    
    #else:

