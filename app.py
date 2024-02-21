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
    credit_rwa = st.slider('CREDIT RWA', 0, 100000000000, 100000)
    operational_rwa = st.slider('OPERATIONAL RWA', 0, 10000000000,100000)
    market_rwa = st.slider('MARKET RWA', 0, 10000000000,100000)
    rwa = st.slider('RWA', 0, 10000000000,100000)
    capital = st.slider('capital', 0, 10000000000,100000)

st.text('')
st.text('')
st.text('')
st.text('')

with col2:
    st.text("capital tier characteristics")
    capital_tier2 = st.slider('capital_tier2', 0, 100000000000, 100000)
    total_qualifying_capital = st.slider('total_qualifying_capital', 0, 100000000000, 100000)
    tier1_to_twra = st.slider('TIER 1 TO TWRA (%)', 0, 100000000000, 100000)
    tier2_to_twra = st.slider('TIER 2 TO TWRA (%)', 0, 100000000000, 100000)

if st.button("Predict Capital Adequacy Ratio (CAR)"):
    result = predict(
        np.array([[credit_rwa, 
        operational_rwa, 
        market_rwa, 
        rwa,
        capital,
        capital_tier2,
        total_qualifying_capital,
        tier1_to_twra,
        tier2_to_twra
        ]]))
    
    st.text(f'The Capital Adequacy ratio is {round(result[0], 3)}%')

st.text('')
st.text('')


