import streamlit as st
import pandas as pd
import joblib

st.title("House Price Prediction (PP5)")

st.write("Enter property details to get a predicted sale price.")

# Load model
model = joblib.load("model.pkl")

# Minimal input fields
lot_area = st.number_input("LotArea", min_value=0, value=5000)
gr_liv_area = st.number_input("GrLivArea", min_value=0, value=1500)
garage_area = st.number_input("GarageArea", min_value=0, value=300)

if st.button("Predict Price"):
    # Build minimal input row
    data = {
        "LotArea": [lot_area],
        "GrLivArea": [gr_liv_area],
        "GarageArea": [garage_area],
    }

    df = pd.DataFrame(data)

    # Predict
    prediction = model.predict(df)[0]

    st.success(f"Predicted Sale Price: ${prediction:,.0f}")
