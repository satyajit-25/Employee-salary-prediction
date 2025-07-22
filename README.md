# Employee Salary Prediction Project

## 🌟 Project Overview

This project presents a **Machine Learning Model for Employee Salary Forecasting**, a data-driven solution aimed at predicting employee salaries accurately. By leveraging historical employee data, the model identifies key factors influencing compensation, enabling more standardized, transparent, and fair salary determination within an organization.

The primary goal is to support better HR decision-making, improve employee morale, and ensure the organization remains competitive in the talent market.

## ✨ Capabilities

This project focuses on building a predictive model that can:

* **Forecast Salaries:** Predict an employee's salary based on various attributes.
* **Identify Key Influencers:** Determine which factors (e.g., experience, education, role) have the most significant impact on salary.
* **Support Fair Compensation:** Provide a data-driven baseline for establishing equitable and consistent salary structures.

## 🚀 Technologies Used

The project is built using Python and several powerful libraries:

* **Python:** The core programming language.
* **pandas:** For efficient data manipulation and analysis.
* **numpy:** Essential for numerical operations.
* **scikit-learn:** For machine learning model building, data preprocessing, and evaluation.
* **matplotlib & seaborn:** For data visualization and exploratory data analysis (EDA).

## ⚙️ Setup and Installation

Follow these steps to set up the project locally:

### Prerequisites

* Python 3.x (Recommended: 3.8+)

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/satyajit-25/Employee-salary-prediction.git](https://github.com/satyajit-25/Employee-salary-prediction.git)
    cd Employee-salary-prediction
    ```
    

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv .venv
    ```
    * **On Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

3.  **Install Dependencies:**
    Install all required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## 🏃 How to Run

1.  **Activate your virtual environment** (if you created one).
2.  **Navigate to the project directory** (where your main script and model files are).
3.  **Run the main prediction script** (replace `your_main_script.py` with your actual entry point if it's not named `main_app.py`):
    ```bash
    python your_main_script.py
    ```
    

## 📊 Key Findings & Model Performance

Our model successfully predicts employee salaries with notable accuracy.

* **Best Performing Model:** Random Forest Regressor
* **Key Performance Metrics (Example):**
    * **R-squared (R² Score):** [e.g., 0.9997] - Indicates very high predictability of salary variance.
    * **Mean Absolute Error (MAE):** [e.g., 14.3] - On average, predictions were off by a minimal amount.
    * **Mean Squared Error (MSE):** [e.g., 376.86]

* **Influential Features:** Features like 'Years of Experience', 'Education Level', and 'Role/Department' were identified as the most significant drivers of salary.

## 📈 Exploratory Data Analysis (EDA)
Visualizations from the Exploratory Data Analysis provided critical insights into the dataset, revealing correlations and relationships between various features and employee salaries.

## 🎬 Demo Video

Watch a short demonstration of the AI Computer Vision Toolkit in action:

[https://employee-salary-prediction02.streamlit.app/]

#

# 📸 Screenshots
![Correlation Heatmap of Data](https://github.com/satyajit-25/Employee-salary-prediction/blob/main/Result/newplot.png)
## 

![Relationship Between Numerical Data](https://github.com/satyajit-25/Employee-salary-prediction/blob/main/Result/newplot%20(1).png)
## 

![Feature Relation](https://github.com/satyajit-25/Employee-salary-prediction/blob/main/Result/newplot%20(2).png)
# 


## 🔗 GitHub Repository

Access the complete source code, data (if applicable and anonymized), and the trained model file (`random_forest_regressor_salary_predictor_v4.pkl`) here:

[https://github.com/satyajit-25/Employee-salary-prediction](https://github.com/satyajit-25/Employee-salary-prediction)

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
