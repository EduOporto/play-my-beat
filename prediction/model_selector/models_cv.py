import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, HistGradientBoostingRegressor, VotingRegressor, StackingRegressor
from sklearn.svm import SVR
from sklearn.model_selection import cross_validate
import xgboost as xgb
from sklearn.neighbors import KNeighborsRegressor, RadiusNeighborsRegressor, KDTree

def modeling(X, y, cv):
    
    r_models = [LinearRegression(), DecisionTreeRegressor(), RandomForestRegressor(), 
                SVR(kernel='rbf'), Ridge(), GradientBoostingRegressor(), xgb.XGBRegressor(), 
                KNeighborsRegressor(), RadiusNeighborsRegressor(), AdaBoostRegressor(), 
                HistGradientBoostingRegressor()]

    r2_score = []
    rmse = []
    
    for model in r_models:
        results = cross_validate(model, X, y, scoring=('neg_root_mean_squared_error', 'r2'), cv=cv)

        rmse.append(-results['test_neg_root_mean_squared_error'].mean())
        r2_score.append(results['test_r2'].mean())
    
    df = pd.DataFrame({'model': ['Linear Regression', 
                                        'Decission Tree', 
                                        'Random Forest Regressor', 
                                        'Support Vector Machine', 
                                        'Ridge Regression', 
                                        'Gradient Boost Regression',
                                        'XGboost Regression',
                                        'K Nearest Neighbors',
                                        'Radius Neighbors',
                                        'Ada Boost Regressor',
                                        'Hist Gradien Boost Regression'],
                            'RMSE': rmse,
                            'R^2': r2_score}
                        )

    return df.sort_values(['RMSE'])

