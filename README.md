# 📊 Telco Customer Churn Prediction & Analytics Dashboard

[![Live Demo](https://img.shields.io/badge/Streamlit_App-Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit)](https://telco-customer-churn-eshwar2206.streamlit.app/)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/Model-XGBoost-0052CC?style=for-the-badge)](https://xgboost.readthedocs.io/)

An end-to-end Machine Learning web application designed to predict customer churn probability for telecommunication providers. Built with Python, XGBoost, and Optuna, and deployed via Streamlit Cloud.

---

## 🚀 Live Demo
Access the interactive web dashboard here: **[Telco Customer Churn Predictor](https://telco-customer-churn-eshwar2206.streamlit.app/)**

---

## 📌 Project Architecture & Workflow
Raw CSV Data (7043 rows)
├──> Preprocessing & Feature Engineering
├──> Class Imbalance Handling (scale_pos_weight = 2.77)
├──> Stratified 5-Fold Cross-Validation
├──> Optuna Hyperparameter Optimization (30 Trials)
├──> Model Pipeline Serialization (.pkl)
└──> Streamlit Cloud Deployment


---

## 💡 Key Technical Features

1. **Class Imbalance Management:** Computed a custom `scale_pos_weight` ratio ($0.73 : 0.27$) to optimize minority class recall without synthetic data distortion.
2. **Domain-Specific Feature Engineering:**
   - `Charge_Ratio`: Ratio of Total Charges to Monthly Charges.
   - `Tenure_Group`: Ordinal lifecycle binning (`0-1 Yr`, `1-2 Yrs`, `2-4 Yrs`, `4-5 Yrs`, `5+ Yrs`).
   - `Total_Services`: Cumulative active add-on subscriptions count.
3. **Hyperparameter Tuning:** Automated 30 Optuna trial searches, achieving a final **AUC-ROC of 0.848** on cross-validation.
4. **Data Leakage Prevention:** Encapsulated `StandardScaler` and `OneHotEncoder` inside scikit-learn `Pipeline` objects across training folds.

---

## 🛠️ Tech Stack & Dependencies

- **Data Wrangling:** `pandas`, `numpy`
- **Machine Learning & Tuning:** `scikit-learn`, `xgboost`, `optuna`
- **Model Persistence:** `joblib`
- **Web App & Hosting:** `streamlit`, Streamlit Community Cloud

---

## ⚙️ How to Run Locally


# 1. Clone the repository
git clone [https://github.com/eshwar2206/telco-customer-churn.git](https://github.com/eshwar2206/telco-customer-churn.git)
cd telco-customer-churn

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Streamlit dashboard
streamlit run app.py

---

### Task 2: Configure Repository "About" Metadata

On your [GitHub Repository main page](https://github.com/eshwar2206/telco-customer-churn):
1. Click the **gear icon** ($\text{⚙️}$) next to the **About** section on the right-hand sidebar.
2. Fill in the following fields:
   * **Description:** *End-to-end Machine Learning pipeline & Streamlit dashboard for predicting customer churn using XGBoost & Optuna.*
   * **Website:** `[https://telco-customer-churn-eshwar2206.streamlit.app/](https://telco-customer-churn-eshwar2206.streamlit.app/)`
   * **Topics:** `machine-learning`, `xgboost`, `optuna`, `streamlit`, `churn-prediction`, `data-science`
3. Click **Save changes**.

---

### Task 3: Pin the Repository to Your GitHub Profile

1. Navigate to your main [GitHub Profile](https://github.com/eshwar2206).
2. Click **Customize your pins** (or **Edit pins**).
3. Select **`telco-customer-churn`** and click **Save pins**.

---

### Project 1 Completed!

Your first project is fully deployed, documented, and ready to show to recruiters.

When you are ready, let me know to move on to **Project 2: Retail & Inventory Analytics Dashboard (Data Analy
