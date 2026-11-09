import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def app():

    st.title("📊 Correlation Study")

    st.markdown("""
    ## Correlation Analysis

    This page explores the relationships between house
    characteristics and SalePrice using the Ames Housing Dataset.
    """)

    # Load data
    df = pd.read_csv(
        "house-prices-advanced-regression-techniques/train.csv"
    )

    # Numeric correlations
    corr = df.corr(numeric_only=True)["SalePrice"]

    top_corr = (
        corr.abs()
        .sort_values(ascending=False)
        .drop("SalePrice")
        .head(10)
    )

    st.subheader("Top 10 Features Correlated with SalePrice")

    st.dataframe(top_corr)

    # Bar chart
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(
        x=top_corr.values,
        y=top_corr.index,
        ax=ax
    )

    ax.set_title("Top Features Correlated with SalePrice")
    ax.set_xlabel("Correlation Strength")
    ax.set_ylabel("Feature")

    st.pyplot(fig)

    st.markdown("""
    ## Interpretation

    The chart highlights the variables that show the
    strongest relationship with SalePrice.

    The strongest correlation with SalePrice is OverallQual
    (correlation = 0.791), indicating that higher-quality
    properties generally command higher market prices.

    GrLivArea shows a strong positive relationship with
    SalePrice (correlation = 0.709), suggesting that larger
    living areas tend to increase property value.

    GarageCars and GarageArea both display substantial
    positive correlations, demonstrating that garage
    capacity contributes to overall house valuation.

    These variables are expected to have a significant
    influence on house prices and are therefore important
    predictors for the machine learning model.
    """)
