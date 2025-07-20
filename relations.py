import streamlit as st
import pandas as pd
import plotly.express as px


st.markdown("""
    <style>
    .custom-box {
        background-color: #1C1C1E;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 0 15px rgba(160,32,240,0.3);
    }
    .custom-header {
        color: #A020F0;
        font-size: 26px;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

def create_heat_map(the_df):
    
    correlation = the_df.corr(numeric_only=True)
    fig = px.imshow(
        correlation,
        template="plotly_dark",
        text_auto="0.2f",
        aspect=1,
        color_continuous_scale="purpor",
        title="Correlation Heatmap of Data",
        height=650,
    )
    fig.update_traces(textfont={"size": 16, "family": "consolas"})
    fig.update_layout(
        title={"font": {"size": 30, "family": "tahoma"}},
        hoverlabel={"bgcolor": "#111", "font_size": 15, "font_family": "consolas"}
    )
    return fig

def create_scatter_matrix(the_df):
    fig = px.scatter_matrix(
        the_df,
        dimensions=the_df.select_dtypes(include="number").columns,
        height=800,
        color=the_df.iloc[:, -1],
        opacity=0.65,
        title="Relationships Between Numerical Data",
        template="plotly_dark"
    )
    fig.update_layout(
        title={"font": {"size": 30, "family": "tahoma"}},
        hoverlabel={"bgcolor": "#111", "font_size": 14, "font_family": "consolas"}
    )
    return fig

def create_relation_scatter(the_df, x, y):
    fig = px.scatter(
        data_frame=the_df,
        x=x,
        y=y,
        color=y,
        opacity=0.78,
        title="Feature Relation: {} vs. {}".format(x, y),
        template="plotly_dark",
        trendline="ols",
        height=650
    )
    fig.update_layout(title={"font": {"size": 28, "family": "tahoma"}})
    return fig

def run():
    st.title("📊 Feature Relations & Correlations")

    if "uploaded_dataset_path" in st.session_state:
        df = pd.read_csv(st.session_state["uploaded_dataset_path"])
    else:
        df = pd.read_csv("Cleaned_Salary_Data.csv")  # fallback dataset

     # Keep only numeric columns
    numeric_df = df.select_dtypes(include=["number"])


    with st.container():
        st.plotly_chart(create_heat_map(numeric_df), use_container_width=True)

    with st.container():
        st.plotly_chart(create_scatter_matrix(numeric_df), use_container_width=True)

    with st.container():
        numeric_cols = numeric_df.columns.tolist()

        col1, col2 = st.columns(2)
        with col1:
            x_feat = st.selectbox("Select X-Axis Feature", numeric_cols, key="x")
        with col2:
            y_feat_options = [col for col in numeric_cols if col != x_feat]
            y_feat = st.selectbox("Select Y-Axis Feature", y_feat_options, key="y")

        if x_feat and y_feat:
            st.plotly_chart(create_relation_scatter(df, x_feat, y_feat), use_container_width=True)
