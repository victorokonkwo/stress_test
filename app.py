import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict


st.title('Capital Adequecy Model')
st.markdown('CAR model prediction for stress testing.')

st.header("Stress Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.text("non-interest characteristics")
    total_noninterest_expense_reported = st.slider('total noninterest expense reported', 0, 1000000000, 1000000)
    total_noninterest_income_reported = st.slider('total noninterest income reported', 0, 1000000000,1000000)

with col2:
    st.text("interest characteristics")
    total_interest_expense_reported = st.slider('total interest expense reported', 0, 1000000000, 1000000)
    total_interest_income_reported = st.slider('total interest income reported', 0, 1000000000, 1000000)

with col3:
    st.text("loss characteristics")
    provision_losses = st.slider('provision.losses', 0, 1000000000, 1000000)
  

st.text('')
if st.button("Predict Capital Adequecy Ratio (CAR)"):
    result = predict(
        np.array([[total_noninterest_expense_reported, 
        total_noninterest_income_reported, 
        total_interest_expense_reported, 
        total_interest_income_reported,
        provision_losses
        ]]))
    
    st.text(f'The capital adequecy ratio is {round(result[0], 3)}%')

st.text('')
st.text('')