from statsmodels.tsa.statespace.sarimax import SARIMAX
import itertools
import pandas as pd

def grid_search(df, min_obs):
    y = df.bpm

    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], min_obs) for x in list(itertools.product(p, d, q))]

    results_dict = {'AIC': [], 'param': [], 'param_seas': []}

    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = SARIMAX(y, 
                            order=param, 
                            seasonal_order=param_seasonal, 
                            enforce_stationarity=False, 
                            enforce_invertibility=False)

                results = mod.fit()
                results_dict['AIC'].append(results.aic)
                results_dict['param'].append(param)
                results_dict['param_seas'].append(param_seasonal)
            except:
                continue

    results_df = pd.DataFrame(results_dict).sort_values('AIC').head(1)

    return results_df['param'].values[0], results_df['param_seas'].values[0]

