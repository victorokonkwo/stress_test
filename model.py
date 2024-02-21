import os 
import numpy as np
import pandas as pd 
import joblib
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error



# random seed
seed = 42

car = pd.read_excel('data/Model Testing.xlsx')
car = car.drop([1,2]).reset_index(drop=True)
columns_rename = car.drop([1,2]).reset_index(drop=True).iloc[0, :].to_dict()

columns_rename['Unnamed: 7'] = 'CAPITAL_TIER2'
columns_rename['Unnamed: 1'] = 'MONTH'

car = car.rename(columns=columns_rename).drop(0)
columns = [
'CREDIT RWA',
'OPERATIONAL RWA',
'MARKET RWA',
'TRWA',
'CAPITAL',
'CAPITAL_TIER2',
'TOTAL QUALIFYING CAPITAL',
 'TIER 1 TO TWRA (%)',
'TIER 2 TO TWRA (%)',
 'CAR (%)'
]

new_df = car[columns]

model_xgb = XGBRegressor(random_state=seed)
for col in new_df.columns:
    new_df[col] = new_df[col].astype(float) 

X = new_df.drop('CAR (%)', axis=1)
y = new_df['CAR (%)']

model_xgb.fit(X, y)

# save the model to disk
joblib.dump(model_xgb, "xgb_model.sav")
