# 🏥 Health Insurance Premium Prediction System

An end-to-end machine learning application that predicts health insurance premiums based on user demographics, lifestyle, and medical history. This project combines **feature engineering, model segmentation, and an interactive web interface** to deliver accurate and user-friendly predictions.

---

## 🚀 Highlights

- 🔢 Real-time premium prediction via Streamlit  
- 🧠 **Segmented ML architecture**:
  - Separate models for different age groups (≤25 and >25)
- 🧬 Custom **medical risk scoring system**
- ⚙️ Full preprocessing pipeline (encoding + scaling)
- 📊 Structured feature engineering for improved model performance  
- 🎯 Clean and interactive UI with reset functionality and animations  

---

## 🧠 Machine Learning Approach

### 1. Problem Type
- Supervised Learning  
- Regression problem (predicting continuous premium value)

---

### 2. Feature Engineering

A key highlight of this project is the **custom normalized risk score**:

- Converts medical history into numerical risk  
- Supports multiple conditions (e.g., *Diabetes & High Blood Pressure*)  
- Weighted scoring system:
  - Heart disease → high risk  
  - Diabetes / BP → medium risk  
  - Thyroid → lower risk  
- Normalized to range **[0, 1]**

---

### 3. Model Segmentation

Instead of using a single model:

- **Model 1 (Young Users ≤ 25)**  
- **Model 2 (Adults > 25)**  

This improves prediction accuracy by capturing different risk patterns across age groups.

---

### 4. Preprocessing Pipeline

- Manual one-hot encoding for categorical variables  
- Plan encoding (Bronze → 1, Silver → 2, Gold → 3)  
- Age-based dynamic scaling using separate scalers  
- Ensures consistent feature structure for model input  

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Machine Learning:** Scikit-learn  
- **Model Persistence:** Joblib  
- **Data Processing:** Pandas, NumPy  

---

## 📊 Workflow

1. User inputs personal, health, and policy details  
2. Medical history is converted into a normalized risk score  
3. Data is encoded and scaled dynamically  
4. Based on age:
   - Young model OR Adult model is selected  
5. Model predicts insurance premium  
6. Result is displayed via an interactive UI  

---

## 📦 Installation & Setup

```bash
git clone https://github.com/Saurabh136/ML_Project_Health_Insurance_Premium_Predictor.git
cd <project-folder>
pip install -r requirements.txt
streamlit run main.py

