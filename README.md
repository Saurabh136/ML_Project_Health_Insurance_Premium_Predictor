# 🏥 Health Insurance Premium Prediction System

## 🌐 Live Application

🚀 **Try the app here:**  
👉 https://ml-project-health-insurance-premium-predictor.streamlit.app/ 
[![Live App](https://img.shields.io/badge/Live-App-green)](https://ml-project-health-insurance-premium-predictor.streamlit.app/)

_No installation required — works directly in your browser._

---

## 🚀 Highlights

- 🔢 Real-time insurance premium prediction  
- 🧠 **Segmented ML architecture** (age-based models)  
- 🧬 Custom **Genetic Risk feature engineering**  
- ⚙️ End-to-end preprocessing pipeline (encoding + scaling)  
- 🎯 Clean and interactive UI built with Streamlit  
- 🔄 Fully functional reset (true form reset using key-versioning)  
- ⚡ Smooth user experience with responsive design  

---

## 🧠 Machine Learning Approach

### 1. Problem Type
- Supervised Learning  
- Regression (predicting continuous insurance premium)

---

### 2. Feature Engineering

A key highlight of this project is the **custom normalized medical risk score**:

- Converts medical history into numerical values  
- Handles multiple conditions (e.g., *Diabetes & High BP*)  
- Weighted scoring system:
  - Heart disease → high risk  
  - Diabetes / BP → medium risk  
  - Thyroid → lower risk  
- Normalized to range **[0, 1]**

---

### 3. Model Segmentation

Instead of using a single model:

- **Model 1 → Young Users (≤ 25)**  
- **Model 2 → Adults (> 25)**  

👉 This improves prediction accuracy by capturing different behavioral and health risk patterns.

---

### 4. Preprocessing Pipeline

- Manual one-hot encoding for categorical variables  
- Insurance plan encoding:
  - Bronze → 1  
  - Silver → 2  
  - Gold → 3  
- Age-based scaling using separate scalers  
- Ensures consistent feature structure for model input  

---

## 📊 Model Performance & Impact of Feature Engineering

### 🔹 Young Model (≤ 25) — Before Genetic Risk

| Model | Train Score | Test Score |
|------|------------|-----------|
| Linear Regression | 0.6020 | 0.6047 |
| XGBoost | ~0.603 | ~0.60 |

- ⚠️ **Extreme Error (>10%)**: **73%**

---

### 🔹 Young Model (≤ 25) — After Genetic Risk

| Model | Train Score | Test Score |
|------|------------|-----------|
| Linear Regression | 0.9882 | 0.9887 |
| XGBoost | ~0.987 | ~0.98 |

- ✅ **Extreme Error (>10%) reduced to: ~2%**

---

### 🔹 Rest Model (> 25)

| Model | Train Score | Test Score |
|------|------------|-----------|
| Linear / Ridge Regression | ~0.953 | ~0.953 |
| XGBoost | ~0.994 |

- ✅ **Extreme Error (>10%)**: **~0.3%**

---

## 🎯 Key Insight

The introduction of the **Genetic Risk feature** led to a **massive performance improvement** for the young age group:

- 📉 Extreme error reduced from **73% → 2%**  
- 📈 Model accuracy improved from ~0.60 → ~0.98  

👉 This demonstrates the **critical role of domain-specific feature engineering in machine learning performance**

---

## 📊 Application Workflow

1. User enters personal, health, and policy details  
2. Medical history → converted into normalized risk score  
3. Data → encoded and scaled  
4. Model selection based on age  
5. Prediction generated  
6. Result displayed via interactive UI  

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Machine Learning:** Scikit-learn, XGBoost  
- **Model Storage:** Joblib  
- **Data Processing:** Pandas, NumPy  

---

## 🔁 Reset Functionality (Key Highlight)

A true reset functionality was implemented using **dynamic key versioning**:

- Streamlit widgets retain state by default  
- Instead of clearing state, widget keys are dynamically changed  
- This forces reinitialization of all inputs  

👉 Result: behaves like a full page refresh

---

## 📦 Installation & Setup

```bash
git clone https://github.com/Saurabh136/ML_Project_Health_Insurance_Premium_Predictor.git
cd <project-folder>
pip install -r requirements.txt
streamlit run main.py
