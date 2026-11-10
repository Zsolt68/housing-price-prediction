import streamlit as st
import joblib


def app():

    st.title("Model Verification")

    st.write(
        "This page verifies that the trained model "
        "and feature columns load correctly."
    )

    try:

        model = joblib.load("model.pkl")
        st.success("model.pkl loaded successfully.")

        X_train_columns = joblib.load("xtrain_columns.pkl")
        st.success("xtrain_columns.pkl loaded successfully.")

        st.write(
            f"Number of training features: "
            f"**{len(X_train_columns)}**"
        )

        st.write("Model parameters:")
        st.json(model.get_params())

        st.markdown("---")

        st.header("Model Performance")

        st.markdown("""
        ## Business Case Evaluation

        Success Metric:

        - R² ≥ 0.75

        Model Result:

        - R² = 0.8895

        The model exceeds the business performance target and
        demonstrates strong predictive capability for estimating
        residential property sale prices.
        """)

        st.subheader("Evaluation Metrics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="R² Score",
                value="0.8895"
            )

        with col2:
            st.metric(
                label="Mean Absolute Error (MAE)",
                value="$17,577"
            )

        st.markdown("""
        ## Interpretation

        The model achieved an **R² score of 0.8895**,
        meaning it explains approximately **88.95%**
        of the variation in house prices.

        The **Mean Absolute Error (MAE)** of approximately
        **$17,577** indicates that predictions are
        typically within that amount of the actual
        sale price.

        These results suggest that the Random Forest
        Regressor provides strong predictive performance
        for the Ames Housing Dataset and exceeds the
        project's success threshold of **R² ≥ 0.75**.
        """)

    except Exception as e:

        st.error(
            f"Error loading model or columns: {e}"
        )