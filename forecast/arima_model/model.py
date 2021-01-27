from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
import pandas as pd

def get_prediction(df, order, seasonal_order):
    mod = SARIMAX(df,
              order=order,
              seasonal_order=seasonal_order,
              enforce_stationarity=False,
              enforce_invertibility=False)

    results = mod.fit(disp=False)

    pred = results.get_prediction(start=pd.to_datetime('1970-01-10'), dynamic=False)
    pred_ci = pred.conf_int()

    ax = df['1970-01-10':].plot(label='observed')
    pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))

    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.2)
    ax.set_xlabel('Date')
    ax.set_ylabel('BPM')
    plt.legend()

    prediction = pd.DataFrame(pred.predicted_mean)

    prediction.to_csv('model/predictions/prediction.csv')
    pred_ci.to_csv('model/predictions/predicted_ci.csv')

    print("""\n
    A new prediction has been saved!""")

    return plt.show()
    