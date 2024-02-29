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


# Income
data = pd.read_excel('data/Model Testing.xlsx', sheet_name='Income').T
data = data.drop([0,1,2,3,4], axis=1)
data = data.drop('Unnamed: 0')

data_income = data.reset_index(drop=True)
column = list(data_income.columns)
col_rename = data_income.iloc[0, :].to_dict()

data_income = data_income.rename(columns=col_rename)
data_income = data_income.drop(0)

data_income.to_csv('data_income.csv', index=False)

for col in data_income.columns:
    data_income[col] = data_income[col].astype(float)

X = data_income[['30330:Trading income on Foreign Exchange',
'30210:Interest Expense on Inter-Bank Transactions',
'30290:Total Fees & Commission Income',
'30340:Trading income on Fixed Income securities',
'30150:Income from inter-Bank Transactions',        
'30260:Commissions',                                      
'30120:Interest income on Loans',                         
'30140:Income from Government Securities '
]]


y = data_income['30600:PROFIT/(LOSS) AFTER TAX']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model_PandL = XGBRegressor(random_state=42)
model_PandL.fit(X, y)

joblib.dump(model_PandL, "pandl_model.sav")