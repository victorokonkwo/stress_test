import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict


st.title('Income Model')
st.markdown('Income model prediction for stress testing.')

st.header("Stress Features")

col1, col2 = st.columns(2)

with col1:
    st.text("Income characteristics")
    trading_income = st.text_input('Trading income on Foreign Exchange', value='')
    intrest_expense = st.text_input(':Interest Expense on Inter-Bank Transactions', value='')
    total_fees = st.text_input('Total Fees & Commission Income', value='')
    trading_income_fixed = st.text_input('Trading income on Fixed Income securities', value='')

st.text('')
st.text('')
st.text('')
st.text('')

with col2:
    st.text("Other Characteristics")
    income_inter_bank = st.text_input('Income from inter-Bank Transactions', value='')
    commission = st.text_input('Commissions', value='')
    interest_income = st.text_input('Interest income on Loans', value='')
    income_govt_securities = st.text_input('Income from Government Securities ', value='')

if st.button("Predict PROFIT/(LOSS) AFTER TAX "):
    result = predict(
        np.array([[float(trading_income), 
        float(intrest_expense), 
        float(total_fees), 
        float(trading_income_fixed),
        float(income_inter_bank),
        float(commission),
        float(interest_income),
        float(income_govt_securities)
        ]]),   model="pandl_model.sav")
    
    st.text(f'The PROFIT/(LOSS) AFTER TAX is {round(result[0], 3)}%')

st.text('')
st.text('')