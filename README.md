

<h1 align="center">💼 Salary Prediction App</h1>

<p align="center">
  🚀 A web-based ML application to predict salaries using Ensemble Learning and Streamlit.
</p>

---

## 📌 Table of Contents

- [Overview](#rocket-overview)
- [Features](#-features)
- [Tech Stack](#️-technologies-used)
- [Installation](#clipboard-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Live Demo](#-live-deployment)
- [Snapshots](#-snapshots)
- [Contribution](#-contribution)
- [Author](#-author)

---

## 🚀 Overview

The **Salary Prediction App** is an interactive web application built using **Streamlit**. It leverages an **Ensemble Machine Learning model** to estimate salaries based on user inputs such as **age, education level, experience, and job title**.

It demonstrates the **end-to-end ML lifecycle**: data preprocessing, model training, and frontend integration.

---

## ✨ Features

- 📊 **Interactive UI** – Built using Streamlit with real-time predictions.
- 🧠 **Ensemble Learning** – Trained with multiple models for better accuracy.
- 📝 **User Inputs** – Accepts age, experience, education, and job title.
- 📈 **Model Comparison & Analysis** – Documented in Jupyter Notebooks.
- 📂 **Real-world Dataset** – Based on `Salary_Data.csv`.

---

## 🛠️ Technologies Used

| Purpose              | Tools / Libraries               |
|----------------------|---------------------------------|
| **Frontend**         | Streamlit                       |
| **Backend**          | Python                          |
| **ML & Analysis**    | `scikit-learn`, `pandas`, `numpy` |
| **Visualization**    | `matplotlib`, `seaborn`         |
| **Environment**      | `venv` (Python Virtual Env)     |

---

## 📋 Installation

### ✅ Prerequisites

- Python ≥ 3.8
- pip installed

### 📦 Setup Instructions

```bash
# Step 1: Clone the repository
git clone https://github.com/Shiwansh2601/Salary-Prediction-App.git
cd Salary-Prediction-App

# Step 2: Create and activate a virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt
````

---

## 🏃 Usage

Launch the app locally using:

```bash
streamlit run app.py
```

Then open your browser and visit: [http://localhost:8501](http://localhost:8501)

Fill in the sidebar form to get an instant **salary prediction**!

---

## 📂 Project Structure

```
📁 Salary-Prediction-App/
├── .gitignore
├── app.py
├── requirements.txt
├── Salary_Data.csv
├── salary_prediction_model.pkl
├── 01_Salary_Prediction_Model_Comparison.ipynb
├── 02_Salary_Prediction_FinalModel_for_App.ipynb
├── image/
│   ├── actual vs prediction.png
│   └── app Output.png
└── README.md
```

---

## 🔗 Live Deployment

🌐 **Try the App Live**:
👉 [Click here to open the deployed app](https://salarypredictiona.streamlit.app/)

---

## 📸 Snapshots

### 📘 Model Comparison Notebook

<p align="center">
  <img src="https://github.com/Shiwansh2601/Salary-Prediction-App/blob/main/image/actual%20vs%20prediction.png" alt="Model Comparison" width="80%">
</p>

### 🖥️ Streamlit App Output

<p align="center">
  <img src="https://github.com/Shiwansh2601/Salary-Prediction-App/blob/main/image/app%20Output.png" alt="App Output" width="80%">
</p>

---

## 🤝 Contribution

👋 Pull requests are welcome!

If you encounter a bug or have a feature request, please [open an issue](https://github.com/Shiwansh2601/Salary-Prediction-App/issues) or submit a PR.

---

## 👨‍💻 Author

**Shiwansh Tiwari**

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:9b00e8,100:6e44ff&height=100&section=footer"/>
</p>


