import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict


st.title('Capital Adequacy Model')
st.markdown('CAR model prediction for stress testing.')

st.header("Stress Features")

col1, col2 = st.columns(2)

with col1:
    st.text("RWA characteristics")
    # credit_rwa = st.slider('CREDIT RWA', 0, 100000000000, 100000)
    # operational_rwa = st.slider('OPERATIONAL RWA', 0, 10000000000,100000)
    # market_rwa = st.slider('MARKET RWA', 0, 10000000000,100000)
    # rwa = st.slider('RWA', 0, 10000000000,100000)
    # capital = st.slider('capital', 0, 10000000000,100000)
    credit_rwa = st.text_input('CREDIT RWA', value='0')
    operational_rwa = st.text_input('OPERATIONAL RWA', value='0')
    market_rwa = st.text_input('MARKET RWA', value='0')
    rwa = st.text_input('RWA', value='0')
    capital = st.text_input('capital', value='0')





st.text('')
st.text('')
st.text('')
st.text('')

with col2:
    st.text("Capital Tier Characteristics")
    # capital_tier2 = st.slider('Capital Tier2', 0, 100000000000, 100000)
    # total_qualifying_capital = st.slider('Total Qualifying Capital', 0, 100000000000, 100000)
    # tier1_to_twra = st.slider('TIER 1 TO TWRA (%)', 0, 100000000000, 100000)
    # tier2_to_twra = st.slider('TIER 2 TO TWRA (%)', 0, 100000000000, 100000)
    capital_tier2 = st.text_input('Capital Tier2', value='0')
    total_qualifying_capital = st.text_input('Total Qualifying Capital', value='0')
    tier1_to_twra = st.text_input('TIER 1 TO TWRA (%)', value='0')
    tier2_to_twra = st.text_input('TIER 2 TO TWRA (%)', value='0')

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
        ]]))
    
    st.text(f'The Capital Adequacy ratio is {round(result[0], 3)}%')

st.text('')
st.text('')


