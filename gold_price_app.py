import streamlit as st
import numpy as np
import joblib

# Load the model and scaler
model = joblib.load('GoldPrice_model.pkl')
scaler = joblib.load('slr.pkl')  



# Streamlit App
st.title("Gold Price Prediction")
st.write("Enter the following details to predict the gold price (GLD).")

# Input fields
spx = st.number_input("S&P 500 Index (SPX)", min_value=0.0, format="%.2f")
uso = st.number_input("Crude Oil ETF (USO)", min_value=0.0, format="%.2f")
slv = st.number_input("Silver ETF (SLV)", min_value=0.0, format="%.2f")
eur_usd = st.number_input("Exchange Rate (EUR/USD)", format="%.5f")
year = st.number_input("Year", min_value=2000, max_value=2030, step=1)
month = st.slider("Month", 1, 12, 1)
day = st.slider("Day", 1, 31, 1)
day_of_week = st.slider("Day of the Week", 0, 6, 0)

# Prediction    
if st.button("Predict Gold Price"):
    input_features = np.array([[spx, uso, slv, eur_usd, year, month, day, day_of_week]])
    
    # Apply the scaler to the input features
    scaled_features = scaler.transform(input_features)
    
    # Predict using the trained model
    prediction = model.predict(scaled_features)[0]
    
    st.success(f"Predicted Gold Price (GLD): ${prediction:.2f}")
