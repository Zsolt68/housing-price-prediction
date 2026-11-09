import streamlit as st


def app():

    st.title("🔬 Hypothesis Validation")

    st.markdown("""
    ## Project Hypotheses

    The following hypotheses were developed based on the business
    requirements and exploratory data analysis performed on the
    Ames Housing Dataset.
    """)

    st.markdown("""
    ### Hypothesis 1

    **Properties with larger living areas tend to have higher sale prices.**

    #### Validation

    Correlation analysis identified a strong positive relationship
    between GrLivArea and SalePrice.

    Correlation coefficient:

    **0.709**

    #### Conclusion

    ✅ Supported

    Larger residential properties generally achieve higher market values.
    """)

    st.markdown("---")

    st.markdown("""
    ### Hypothesis 2

    **Higher quality houses tend to sell for higher prices.**

    #### Validation

    Correlation analysis showed that OverallQual has the strongest
    relationship with SalePrice.

    Correlation coefficient:

    **0.791**

    #### Conclusion

    ✅ Supported

    Property quality is one of the most important predictors of
    house price.
    """)

    st.markdown("---")

    st.markdown("""
    ### Hypothesis 3

    **Newer houses tend to achieve higher sale prices.**

    #### Validation

    YearBuilt demonstrated a positive correlation with SalePrice.

    Correlation coefficient:

    **0.523**

    #### Conclusion

    ✅ Partially Supported

    Newer properties generally sell for higher prices, although
    other factors such as quality and living area also have a
    significant impact.
    """)

    st.markdown("---")

    st.markdown("""
    ## Overall Findings

    The exploratory analysis supports the original project
    hypotheses.

    Key drivers of property value include:

    - Overall Quality
    - Living Area
    - Garage Capacity
    - Basement Area
    - Property Age

    These findings support the selection of these variables for
    predictive modelling.
    """)

