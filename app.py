import streamlit as st

from app_pages.page_summary import app as page_summary
from app_pages.page_correlation import app as page_correlation
from app_pages.page_hypothesis import app as page_hypothesis
from app_pages.page_ml_model import app as page_ml_model
from app_pages.page_price_prediction import app as page_price_prediction


st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏡",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    (
        "Project Summary",
        "Correlation Study",
        "Hypothesis Validation",
        "ML Performance",
        "House Price Prediction",
    )
)

if page == "Project Summary":
    page_summary()

elif page == "Correlation Study":
    page_correlation()

elif page == "Hypothesis Validation":
    page_hypothesis()

elif page == "ML Performance":
    page_ml_model()

elif page == "House Price Prediction":
    page_price_prediction()
    