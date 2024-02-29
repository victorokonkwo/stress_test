import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict


st.title('Capital Adequacy Model')
st.markdown('CAR model prediction for stress testing.')

st.header("Stress Features")

col1, col2 = st.columns(2)

with col1:
    st.text("TRWA characteristics")
    credit_rwa = st.text_input('CREDIT RWA', value='')
    operational_rwa = st.text_input('OPERATIONAL RWA', value='')
    market_rwa = st.text_input('MARKET RWA', value='')
    rwa = st.text_input('TRWA', value='')

st.text('')
st.text('')
st.text('')
st.text('')

with col2:
    st.text("Capital Tier Characteristics")
    capital = st.text_input('Capital Tier1', value='')
    capital_tier2 = st.text_input('Capital Tier2', value='')
    total_qualifying_capital = st.text_input('Total Qualifying Capital', value='')
    tier1_to_twra = st.text_input('TIER 1 TO TWRA (%)', value='')
    tier2_to_twra = st.text_input('TIER 2 TO TWRA (%)', value='')

if st.button("Predict Capital Adequacy Ratio (CAR)"):
    result = predict(
        np.array([[float(credit_rwa), 
        float(operational_rwa), 
        float(market_rwa), 
        float(rwa),
        float(capital),
        float(capital_tier2),
        float(total_qualifying_capital),
        float(tier1_to_twra),
        float(tier2_to_twra)
        ]]),   model="xgb_model.sav")
    
    st.text(f'The Capital Adequacy ratio is {round(result[0], 3)}%')

st.text('')
st.text('')


