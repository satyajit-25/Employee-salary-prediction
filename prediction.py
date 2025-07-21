import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# =======================
# 📊 Utility Functions
# =======================

if "predict_clicked" not in st.session_state:
    st.session_state["predict_clicked"] = False

def creat_matrix_score_cards(card_image="", card_title="Card Title", card_value=None, percent=False):
    st.image(card_image, caption="", width=70)
    st.subheader(card_title)
    st.subheader(f"{card_value}%" if percent else f"{card_value}")

def create_comparison_df(y_actual, y_pred):
    pred_df = pd.DataFrame()
    pred_df["Actual Salary"] = pd.to_numeric(y_actual, errors="coerce")
    pred_df["Predicted Salary"] = pd.to_numeric(y_pred, errors="coerce")
    pred_df.dropna(inplace=True)
    return pred_df

def create_residules_scatter(pred_df):
    fig = px.scatter(
        pred_df,
        x="Actual Salary",
        y="Predicted Salary",
        color=pred_df["Predicted Salary"] - pred_df["Actual Salary"],
        opacity=0.8,
        title="Predicted vs Actual Salary",
        template="plotly_dark",
        trendline="ols",
        height=650,
        labels={"x": "Actual Salary", "y": "Predicted Salary"}
    )
    fig.update_layout(title={"font": {"size": 28, "family": "tahoma"}})
    return fig

# =======================
# 🚀 Main Prediction UI
# =======================

def run():
    st.header("Prediction Model 💰")

    # Load the model pipeline (which includes preprocessing)
    model = joblib.load("random_forest_regressor_salary_predictor_v4.pkl")

    
    if "prediction_tab" not in st.session_state:
        st.session_state.prediction_tab = "One Entry"

    # Styling the tab-like buttons
    tab_css = """
    <style>
    .tab-container {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
    justify-content: center;
    width: 100%;
    
    }
    .tab-button {
        display: inline-block;
        padding: 0.6em 1.8em;
        margin-right: 10px;
        border-radius: 8px;
        border: 2px solid #A020F0;
        background-color: #1C1C1E;
        color: white;
        font-weight: bold;
        transition: 0.3s ease-in-out;
        cursor: pointer;
        text-align: center;
        flex: 1;  
        padding: 1em 1.5em;
        width: 100% !important;
        max-width: 100% !important;
    }

    .tab-button:hover {
        background-color: #A020F0;
        color: black;
        transform: scale(1.03);
    }

    .tab-active {
        background-color: #A020F0;
        color: black;
        transform: scale(1.03);
    }
    </style>
    """

    st.markdown(tab_css, unsafe_allow_html=True)

    # Render buttons using columns
    col1, col2 = st.columns(2)
    with col1:
        if st.button("One Entry"):
            st.session_state.prediction_tab = "One Entry"
    with col2:
        if st.button("From File"):
            st.session_state.prediction_tab = "From File"


    if st.session_state.prediction_tab == "One Entry":
        
        with st.form("single_prediction_form"):
            container = st.container()
            with container:
                col1, col2 = st.columns(2)
                with col1:
                    age = st.number_input("Employee Age", min_value=18, max_value=65, value=25, step=1)
                with col2:
                    hours = st.number_input("Hours Per Week", min_value=10, max_value=60, value=30, step=1)

                education = st.selectbox("Education", ['Bachelors', 'HS-grad', 'Masters', 'PhD'])
                workclass = st.selectbox("Workclass", ['Private', 'Govt', 'Self-employed'])
                marital = st.selectbox("Marital Status", ['Single', 'Married', 'Divorced'])
                gender = st.selectbox("Gender", ['Male', 'Female'])
                occupation = st.selectbox("Occupation", ['IT', 'Management', 'Sales', 'Support'])
                native_country = st.selectbox("Native Country", ['India', 'Canada', 'USA', 'Others'])

                submit = st.form_submit_button("Predict Salary")
                if submit:
                    st.session_state.predict_clicked = True

        if submit:
            input_df = pd.DataFrame([{
                'age': age,
                'workclass': workclass,
                'education': education,
                'marital-status': marital,
                'occupation': occupation,
                'gender': gender,
                'native-country': native_country,
                'hours-per-week': hours
                }])

            salary = model.predict(input_df)[0]
            with container:
             st.markdown(f"""
     <div style='text-align: center; margin-top: 30px;'>
                    <h2 style='color: white; font-size: 36px;'> Expected Salary : ${salary:,.2f}</h2>
                </div>
""", unsafe_allow_html=True)

    elif st.session_state.prediction_tab == "From File":
        st.warning(
    "⚠️ Please upload your file with the following columns' names in the same order:\n\n"
    "`['Age', 'Education', 'Workclass', 'Occupation', 'Hours Per Week', 'Marital Status', 'Gender', 'Native Country']`"
)
        file = st.file_uploader("Upload CSV File", type="csv")

        if file:
            df = pd.read_csv(file)
            st.dataframe(df.head())

            df = df.dropna()  # Drop rows with missing values

            try:
                predictions = model.predict(df)
                df["Predicted Salary"] = predictions
                st.write("### 💼 Prediction Results")
                st.dataframe(df)

                if st.checkbox("Show Comparison Graph", value=True):
                    if "salary" in df.columns:
                        comp_df = create_comparison_df(df["salary"], df["Predicted Salary"])
                        st.plotly_chart(create_residules_scatter(comp_df))
            except ValueError as e:
                st.error(f"Prediction failed: {e}")
