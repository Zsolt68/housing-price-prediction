import streamlit as st


def app():

    st.title("🏡 House Price Prediction Dashboard")

    st.markdown("""
    ## Project Overview

    This project uses the Ames Housing Dataset to develop a
    machine learning model capable of predicting residential
    property sale prices.

    The project follows a complete predictive analytics
    workflow including:

    - Data Cleaning
    - Feature Engineering
    - Exploratory Data Analysis
    - Machine Learning Modelling
    - Model Evaluation
    - Streamlit Deployment

    ---
    """)

    st.markdown("""
    ## Dataset Content

    The Ames Housing Dataset contains information on 1,460
    residential properties sold in Ames, Iowa.

    Target variable:

    - SalePrice

    Example features include:

    - OverallQual
    - GrLivArea
    - GarageArea
    - TotalBsmtSF
    - YearBuilt
    - Neighborhood
    """)

    st.markdown("""
    ## Business Requirements

    ### Business Requirement 1

    Predict the sale price of residential properties.

    ### Business Requirement 2

    Identify which property features most influence sale price.

    ### Business Requirement 3

    Provide an interactive dashboard that allows users to
    explore the dataset and model performance.
    """)

    st.markdown("""
    ## Dashboard Navigation

    Use the menu on the left to explore:

    - Project Summary
    - Correlation Study
    - Hypothesis Validation
    - ML Performance
    - House Price Prediction
    """)
