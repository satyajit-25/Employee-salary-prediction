import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("Salary_data.csv")

def run():

    
    st.title("Employee Salary Prediction 📈💰🔗")

    try:
        df = load_data()

        # Display a sample
        st.dataframe(df.head(200), use_container_width=True)

        st.write("***")
        st.subheader("Data Summary Overview 🧐")

        num_data = df.select_dtypes(include="number")
        cat_data = df.select_dtypes(include="object")

        if not num_data.empty:
            st.subheader("🔢 Numerical Data Summary")
            st.table(num_data.describe().T)

        if not cat_data.empty:
            st.subheader("🔤 Categorical Data Summary")
            st.table(cat_data.describe().T)

    except FileNotFoundError:
        st.error("❌ Dataset file not found. Please make sure it's uploaded or placed correctly.")
