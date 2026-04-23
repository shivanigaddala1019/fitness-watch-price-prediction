⌚ Fitness Watch Price Prediction System

A Machine Learning project that predicts smartwatch prices based on specifications such as display size, battery life, health tracking features, and connectivity options.

⸻

🚀 Features

* 📊 Data scraping from Flipkart
* 🧹 Data preprocessing & feature engineering
* 📈 Exploratory Data Analysis (EDA)
* 🤖 Multiple ML models:
    * Linear Regression
    * Ridge & Lasso
    * Random Forest
    * Gradient Boosting
    * XGBoost / LightGBM / CatBoost
* 📉 Evaluation Metrics:
    * R² Score
    * MAE
    * RMSE
    * MAPE
* 🌐 Streamlit Web App for prediction

⸻

🏆 Best Model Performance

Gradient Boosting performed best:

* 📈 R² Score: ~0.15
* 📉 MAE: ~800
* 📉 RMSE: ~1400
* 📉 MAPE: ~30%

Note: Performance is moderate due to real-world scraped data limitations.

⸻

🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* CatBoost / XGBoost / LightGBM
* Streamlit
* Matplotlib & Seaborn

⸻

📂 Project Structure
fitness-watch-price-prediction/
│
├── src/
│   ├── app.py
│   ├── model.py
│   ├── preprocess.py
│   ├── eda.py
│
├── data/
├── model.pkl
├── requirements.txt
├── README.md
▶️ Run the Project
pip install -r requirements.txt
streamlit run src/app.py
🎯 Output
* Predict smartwatch price based on user inputs
* Visualize insights using graphs
* Compare multiple ML models

