import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# --- Training Data (Hardcoded Sample or Replace with actual data)
# You can replace this with pd.read_csv('your_file.csv') if using a real file
data = {
    'Age': [32, 28, 45, 36, 52],
    'Education Level': ["Bachelor's", "Master's", "PhD", "Bachelor's", "Master's"],
    'Job Title': ["Software Engineer", "Data Analyst", "Senior Manager", "Sales Associate", "Director"],
    'Years of Experience': [5, 3, 15, 7, 20],
    'Salary': [90000, 65000, 150000, 60000, 200000]
}
df = pd.DataFrame(data)

# --- Feature/Target Split
X = df[['Age', 'Education Level', 'Job Title', 'Years of Experience']]
y = df['Salary']

# --- Preprocessing
categorical_features = ['Education Level', 'Job Title']
numerical_features = ['Age', 'Years of Experience']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'
)

# --- Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# --- Train the model
model.fit(X, y)

# --- Streamlit UI
st.set_page_config(page_title="Salary Predictor", layout="centered")
st.title("💼 Salary Prediction App")
st.markdown("Enter your details to get an estimated salary.")

# --- Input fields
age = st.number_input("Enter your Age", min_value=18, max_value=65, step=1)
experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.5)

education_levels = df['Education Level'].unique().tolist()
job_titles = df['Job Title'].unique().tolist()

education = st.selectbox("Education Level", sorted(education_levels))
job_title = st.selectbox("Job Title", sorted(job_titles))

# --- Predict button
if st.button("Predict Salary"):
    input_df = pd.DataFrame([{
        'Age': age,
        'Education Level': education,
        'Job Title': job_title,
        'Years of Experience': experience
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Salary: ${prediction:,.2f}")
