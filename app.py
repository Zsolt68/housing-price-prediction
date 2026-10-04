import streamlit as st
import pandas as pd
import joblib

st.title("House Price Prediction (PP5)")

st.write("Enter property details to get a predicted sale price.")

# Load model
model = joblib.load("model.pkl")

# --- User Inputs ---
lot_area = st.number_input("Lot Area", min_value=0, value=8000)
gr_liv_area = st.number_input("Above-ground Living Area (GrLivArea)", min_value=0, value=1500)
total_bsmt_sf = st.number_input("Total Basement SF", min_value=0, value=800)
first_flr_sf = st.number_input("1st Floor SF", min_value=0, value=1000)
second_flr_sf = st.number_input("2nd Floor SF", min_value=0, value=500)
open_porch_sf = st.number_input("Open Porch SF", min_value=0, value=50)
enclosed_porch = st.number_input("Enclosed Porch SF", min_value=0, value=0)
three_ssn_porch = st.number_input("3 Season Porch SF", min_value=0, value=0)
screen_porch = st.number_input("Screen Porch SF", min_value=0, value=0)
year_built = st.number_input("Year Built", min_value=1800, value=2000)
yr_sold = st.number_input("Year Sold", min_value=2006, value=2008)
full_bath = st.number_input("Full Bathrooms", min_value=0, value=2)
half_bath = st.number_input("Half Bathrooms", min_value=0, value=1)
bsmt_full_bath = st.number_input("Basement Full Bath", min_value=0, value=0)
bsmt_half_bath = st.number_input("Basement Half Bath", min_value=0, value=0)
garage_area = st.number_input("Garage Area", min_value=0, value=300)

if st.button("Predict Price"):
    # --- Engineered Features ---
    total_sf = total_bsmt_sf + first_flr_sf + second_flr_sf
    total_porch_sf = open_porch_sf + enclosed_porch + three_ssn_porch + screen_porch
    age_at_sale = yr_sold - year_built
    total_bath = full_bath + (0.5 * half_bath) + bsmt_full_bath + (0.5 * bsmt_half_bath)

    # Build input row
    data = {
        "LotArea": [lot_area],
        "GrLivArea": [gr_liv_area],
        "TotalBsmtSF": [total_bsmt_sf],
        "1stFlrSF": [first_flr_sf],
        "2ndFlrSF": [second_flr_sf],
        "OpenPorchSF": [open_porch_sf],
        "EnclosedPorch": [enclosed_porch],
        "3SsnPorch": [three_ssn_porch],
        "ScreenPorch": [screen_porch],
        "YearBuilt": [year_built],
        "YrSold": [yr_sold],
        "FullBath": [full_bath],
        "HalfBath": [half_bath],
        "BsmtFullBath": [bsmt_full_bath],
        "BsmtHalfBath": [bsmt_half_bath],
        "GarageArea": [garage_area],

        # Engineered features
        "TotalSF": [total_sf],
        "TotalPorchSF": [total_porch_sf],
        "AgeAtSale": [age_at_sale],
        "TotalBath": [total_bath],
    }

    df = pd.DataFrame(data)

    # Predict
    prediction = model.predict(df)[0]

    st.success(f"Predicted Sale Price: ${prediction:,.0f}")
