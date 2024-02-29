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
    credit_rwa = st.text_input('Trading income on Foreign Exchange', value='')
    operational_rwa = st.text_input(':Interest Expense on Inter-Bank Transactions', value='')
    market_rwa = st.text_input('Total Fees & Commission Income', value='')
    rwa = st.text_input('Trading income on Fixed Income securities', value='')

st.text('')
st.text('')
st.text('')
st.text('')

with col2:
    st.text("Other Characteristics")
    capital = st.text_input('Income from inter-Bank Transactions', value='')
    capital_tier2 = st.text_input('Commissions', value='')
    total_qualifying_capital = st.text_input('Interest income on Loans', value='')
    tier1_to_twra = st.text_input('Income from Government Securities ', value='')

if st.button("Predict PROFIT/(LOSS) AFTER TAX "):
    result = predict(
        np.array([[float(credit_rwa), 
        float(operational_rwa), 
        float(market_rwa), 
        float(rwa),
        float(capital),
        float(capital_tier2),
        float(total_qualifying_capital),
        float(tier1_to_twra)
        ]]),   model="pandl_model.sav")
    
    st.text(f'The PROFIT/(LOSS) AFTER TAX is {round(result[0], 3)}%')

st.text('')
st.text('')