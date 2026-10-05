import streamlit as st
from app_pages.page_price_prediction import app as price_prediction_page
from app_pages.page_summary import app as summary_page
from app_pages.page_correlation import app as correlation_page
from app_pages.page_hypothesis import app as hypothesis_page
from app_pages.page_ml_model import app as ml_model_page

pages = {
    "Project Summary": summary_page,
    "Price Prediction": price_prediction_page,
    "Correlation Analysis": correlation_page,
    "Hypothesis Testing": hypothesis_page,
    "ML Model": ml_model_page
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))
pages[selection]()
