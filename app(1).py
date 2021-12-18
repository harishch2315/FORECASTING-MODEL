import streamlit as st
import joblib
st.title('FORECASTING MODEL')#title for the web app
forecast = joblib.load('Forecasting Model')#load the model using joblib
st.subheader("select the months using slider")
temp_options=(10,20,30,40,50)
temp=st.select_slider("choose number of months",options=temp_options)
op = forecast.predict([temp])#predict 
if st.button('predict'):
  st.title(op[0]) 
