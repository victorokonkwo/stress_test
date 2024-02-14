from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd 
import joblib

# random seed
seed = 42

nRowsRead = 1000 # specify 'None' if want to read whole file
df1 = pd.read_csv('data/SupervisorySeverelyAdverseDomestic.csv', delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'SupervisorySeverelyAdverseDomestic.csv'
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')

income_hist = pd.read_excel('data/Income_Hist_Data.xlsx')
income_hist['T1CR'] = (income_hist['tier.1.capital.reported'] / income_hist['risk.weighted.assets.reported']) * 100
income_hist = income_hist.rename(columns={'Unnamed: 0': 'timeline'})

income_hist['year'] = income_hist['timeline'].apply(lambda x: x[:4])
bhc_all = income_hist[['year', 'T1CR']].groupby('year').mean().reset_index().sort_values(by='year')

stressed_bhc = income_hist.dropna()
stressed_bhc = stressed_bhc[['year', 'T1CR']].groupby('year').mean().reset_index().sort_values(by='year')

Y9C_bank = pd.read_csv('data/Y9C_banks_all_data_v13.csv')
# bank metric

Y9C_bank['NIC'] = (Y9C_bank['bhck4074'] / Y9C_bank['bhck3368']) * 400
Y9C_bank['NIIC'] = (Y9C_bank['bhck4079'] / Y9C_bank['bhck3368']) * 400
Y9C_bank['NIE'] = (Y9C_bank['bhck4093'] / Y9C_bank['bhck3368']) * 400
Y9C_bank['PPNR'] = ((Y9C_bank['NIC']  + Y9C_bank['NIIC'] - Y9C_bank['NIE']) / Y9C_bank['bhck3368']) * 400
Y9C_bank['NCO'] = ((Y9C_bank['bhck4635'] - Y9C_bank['bhck4605']) / Y9C_bank['bhck3368']) * 400
Y9C_bank['commercial_loan'] = ((Y9C_bank['bhck1763'] + Y9C_bank['bhck1764']) / Y9C_bank['bhck3368']) * 100
Y9C_bank['real_estate_loan'] = (Y9C_bank['bhck1410'] / Y9C_bank['bhck3368']) * 100
Y9C_bank['size'] = Y9C_bank['bhck2170'].apply(lambda x: np.log(x)) 

income_hist['rssd9001'] = income_hist['institution.name'].map({
                                    'Citigroup Inc.': 1951350,
                                    'JPMorgan Chase & Co.': 1039502
                                    })
income_hist_df = income_hist.merge(Y9C_bank, on='rssd9001')

supervisory_df = pd.read_csv('data/SupervisorySeverelyAdverseDomestic.csv')
supervisory_df['Quarter'] = supervisory_df['Date'].apply(lambda x: x.split(' ')[0])
supervisory_df['Year'] = supervisory_df['Date'].apply(lambda x: x.split(' ')[1])
supervisory_df['timeline'] = supervisory_df['Year'] + supervisory_df['Quarter']

total_df = income_hist_df.merge(supervisory_df, on='timeline')
total_df['year'] = total_df['timeline'].apply(lambda x: x[:4])
risk_df = total_df[['year', 'risk.weighted.assets.reported', 'institution.name']].dropna().groupby([
                                                                'year', 'institution.name']).mean().reset_index()
risk_jpmorgan = risk_df[risk_df['institution.name'] == 'JPMorgan Chase & Co.']
risk_df_citi = risk_df[risk_df['institution.name'] == 'Citigroup Inc.']

pred_col = ['total.interes.income.reported',
 'total.interest.expense.reported',
 'total.noninterest.income.reported',
 'total.noninterest.expense.reported',
 'provision.losses',
 'T1CR',
'year',
'institution.name'         
]

total_data = total_df[pred_col].drop_duplicates().dropna()
X = total_data.drop(['T1CR', 'year', 'institution.name'], axis=1)
y = total_data['T1CR']

# x_test = total_data[total_data['institution.name'] == 'JPMorgan Chase & Co.'].drop(['T1CR', 'year', 'institution.name'], axis=1)
# y_test = total_data[total_data['institution.name'] == 'JPMorgan Chase & Co.']['T1CR']

rf = RandomForestRegressor()
rf.fit(X, y)

# save the model to disk
joblib.dump(rf, "rf_model.sav")
