import streamlit as st
import pandas as pd
import joblib

def app():
    st.title("House Price Prediction")

    st.write("Enter property details to get a predicted sale price.")

    # Load model
    model = joblib.load("model.pkl")

    # --- USER INPUTS (RAW FEATURES ONLY — NO ENGINEERED FEATURES) ---
    MSSubClass = st.number_input("MSSubClass", min_value=20, max_value=200, value=60)
    MSZoning = st.selectbox("MSZoning", ["RL", "RM", "FV", "RH", "C (all)"])
    LotFrontage = st.number_input("LotFrontage", min_value=0.0, max_value=200.0, value=70.0)
    LotArea = st.number_input("LotArea", min_value=1000, max_value=50000, value=8000)
    Street = st.selectbox("Street", ["Pave", "Grvl"])
    Alley = st.selectbox("Alley", ["Grvl", "Pave", "None"])
    LotShape = st.selectbox("LotShape", ["Reg", "IR1", "IR2", "IR3"])
    LandContour = st.selectbox("LandContour", ["Lvl", "Bnk", "HLS", "Low"])
    Utilities = st.selectbox("Utilities", ["AllPub", "NoSeWa", "NoSewr", "ELO"])
    LotConfig = st.selectbox("LotConfig", ["Inside", "Corner", "CulDSac", "FR2", "FR3"])
    LandSlope = st.selectbox("LandSlope", ["Gtl", "Mod", "Sev"])
    Neighborhood = st.selectbox("Neighborhood", [
        "CollgCr","Veenker","Crawfor","NoRidge","Mitchel","Somerst","NWAmes","OldTown",
        "BrkSide","Sawyer","NridgHt","IDOTRR","MeadowV","Edwards","Timber","Gilbert",
        "StoneBr","ClearCr","NPkVill","Blmngtn","BrDale","SWISU","Blueste"
    ])
    Condition1 = st.selectbox("Condition1", ["Norm","Feedr","Artery","RRNn","RRAn","PosN","PosA","RRNe","RRAe"])
    Condition2 = st.selectbox("Condition2", ["Norm","Feedr","Artery","RRNn","RRAn","PosN","PosA","RRNe","RRAe"])
    BldgType = st.selectbox("BldgType", ["1Fam","2fmCon","Duplex","Twnhs","TwnhsE"])
    HouseStyle = st.selectbox("HouseStyle", ["1Story","2Story","1.5Fin","1.5Unf","SFoyer","SLvl","2.5Unf","2.5Fin"])
    OverallQual = st.slider("OverallQual", 1, 10, 5)
    OverallCond = st.slider("OverallCond", 1, 10, 5)
    YearBuilt = st.number_input("YearBuilt", min_value=1870, max_value=2020, value=1990)
    YearRemodAdd = st.number_input("YearRemodAdd", min_value=1950, max_value=2020, value=2000)
    GrLivArea = st.number_input("GrLivArea", min_value=300, max_value=6000, value=1500)
    FullBath = st.slider("FullBath", 0, 4, 2)
    HalfBath = st.slider("HalfBath", 0, 2, 1)
    BedroomAbvGr = st.slider("BedroomAbvGr", 0, 6, 3)
    KitchenAbvGr = st.slider("KitchenAbvGr", 0, 3, 1)
    TotRmsAbvGrd = st.slider("TotRmsAbvGrd", 2, 14, 6)
    GarageCars = st.slider("GarageCars", 0, 4, 2)
    GarageArea = st.number_input("GarageArea", min_value=0, max_value=1500, value=400)

    # Build raw input DataFrame
    df = pd.DataFrame({
        "MSSubClass": [MSSubClass],
        "MSZoning": [MSZoning],
        "LotFrontage": [LotFrontage],
        "LotArea": [LotArea],
        "Street": [Street],
        "Alley": [Alley],
        "LotShape": [LotShape],
        "LandContour": [LandContour],
        "Utilities": [Utilities],
        "LotConfig": [LotConfig],
        "LandSlope": [LandSlope],
        "Neighborhood": [Neighborhood],
        "Condition1": [Condition1],
        "Condition2": [Condition2],
        "BldgType": [BldgType],
        "HouseStyle": [HouseStyle],
        "OverallQual": [OverallQual],
        "OverallCond": [OverallCond],
        "YearBuilt": [YearBuilt],
        "YearRemodAdd": [YearRemodAdd],
        "GrLivArea": [GrLivArea],
        "FullBath": [FullBath],
        "HalfBath": [HalfBath],
        "BedroomAbvGr": [BedroomAbvGr],
        "KitchenAbvGr": [KitchenAbvGr],
        "TotRmsAbvGrd": [TotRmsAbvGrd],
        "GarageCars": [GarageCars],
        "GarageArea": [GarageArea]
    })

    # One-hot encode
    df = pd.get_dummies(df, drop_first=True)

    # Align columns with model training data
    # Load X_train columns from feature engineering
    X_train = joblib.load("xtrain_columns.pkl")  # You will create this file

    df = df.reindex(columns=X_train, fill_value=0)

    # Predict
    if st.button("Predict Price"):
        prediction = model.predict(df)[0]
        st.success(f"Estimated Sale Price: ${prediction:,.0f}")
