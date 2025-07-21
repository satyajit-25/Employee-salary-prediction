import streamlit as st
from streamlit_option_menu import option_menu
import os

# Set page config
st.set_page_config(page_title="Prediction Apps", layout="wide")


# Custom Styling
st.markdown("""
    <style>
    /* Rounded glowing buttons */
    .stButton > button {
        border-radius: 12px;
        border: 2px solid #A020F0;
        padding: 0.75em 2em;
        background-color: #1C1C1E;
        color: white;
        transition: 0.3s ease-in-out;
    }

    div.stButton > button {
        width: 100% !important;
        max-width: 100% !important;
        padding: 1em 2em;
        font-size: 1.1rem;
        border-radius: 12px;
        border: 2px solid #A020F0;
        background-color: #1C1C1E;
        color: white;
        transition: 0.3s ease-in-out;
        cursor: pointer;
        text-align: center;
    }

    .stButton > button:hover {
        background-color: #A020F0;
        color: black;
        transform: scale(1.03);
    }

    .stButton > button:focus:not(:active) {
        border-color: rgb(255, 75, 75);
        background-color: #1C1C1E;
        color: rgb(255, 75, 75);
        transform: scale(1.03);
        transition: 0.3s ease-in-out;
    }

    .stSelectbox, .stSlider, .stNumberInput {
        border: none !important;
        box-shadow: none !important;
    }

    .css-1cpxqw2 {
        border: 2px solid #A020F0 !important;
        border-radius: 8px !important;
    }

    .stSelectbox > div > div {
        background-color: #111 !important;
        border: 2px solid #A020F0 !important;
        border-radius: 8px !important;
        color: white !important;
    }

    .sidebar-upload-label {
        margin-top: 40px;
        margin-bottom: 10px;
        font-size: 16px;
        color: white;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with menu + upload
if "uploaded_dataset_path" in st.session_state:
    default_idx = 1  # Automatically open 'Relations & Correlations'
else:
    default_idx = 0  # Default to Home

with st.sidebar:
    selected = option_menu(
        menu_title="Prediction Apps",
        options=["Home", "Relations & Correlations", "Prediction"],
        icons=["house", "bar-chart", "graph-up"],
        menu_icon="cast",
        default_index=default_idx,
    )

    # Upload section styled
    uploaded_file = st.sidebar.file_uploader("📁 Upload Your Dataset", type=["csv"])

if uploaded_file is not None and "uploaded_flag" not in st.session_state:
    # Save file
    os.makedirs("uploaded_files", exist_ok=True)
    file_path = os.path.join("uploaded_files", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Store file path and prevent loop
    st.session_state["uploaded_dataset_path"] = file_path
    st.session_state["uploaded_flag"] = True

    st.rerun()

# Routing
if selected == "Home":
    import home
    home.run()

elif selected == "Relations & Correlations":
    import relations
    relations.run()

elif selected == "Prediction":
    import prediction
    prediction.run()

# ✅ Only delete flag AFTER using it
if "uploaded_flag" in st.session_state:
    del st.session_state["uploaded_flag"]
