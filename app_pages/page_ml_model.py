import streamlit as st
import joblib

def app():
    st.title("Model Verification")

    st.write("This page verifies that the trained model and feature columns load correctly.")

    try:
        model = joblib.load("model.pkl")
        st.success("model.pkl loaded successfully.")

        X_train_columns = joblib.load("xtrain_columns.pkl")
        st.success("xtrain_columns.pkl loaded successfully.")

        st.write(f"Number of training features: **{len(X_train_columns)}**")

        st.write("Model parameters:")
        st.json(model.get_params())

    except Exception as e:
        st.error(f"Error loading model or columns: {e}")
