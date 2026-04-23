import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------
# LOAD DATA + MODEL
# -------------------------
df = pd.read_csv("data/cleaned_data.csv")
model = joblib.load("model.pkl")

st.set_page_config(page_title="Fitness Watch Price Predictor", layout="wide")

st.title("⌚ Fitness Watch Price Prediction System")

# -------------------------
# BRAND MAPPING
# -------------------------
brand_map = {
    0: "Other",
    1: "Noise",
    2: "boAt",
    3: "Fire-Boltt",
    4: "Fastrack"
}

reverse_map = {v: k for k, v in brand_map.items()}

# -------------------------
# INPUT SECTION
# -------------------------
st.subheader("🔧 Enter Watch Features")

col1, col2, col3 = st.columns(3)

with col1:
    brand_name = st.selectbox("Brand", list(brand_map.values()))
    rating = st.slider("Rating", 0.0, 5.0, 3.5)

with col2:
    display_size = st.number_input("Display Size", value=1.8)
    battery_days = st.slider("Battery Days", 1, 30, 7)

with col3:
    calling = st.checkbox("Calling")
    heart_monitor = st.checkbox("Heart Monitor")
    sleep_tracking = st.checkbox("Sleep Tracking")

col4, col5, col6 = st.columns(3)

with col4:
    calories = st.checkbox("Calories Tracking")
    step_counter = st.checkbox("Step Counter")

with col5:
    period_tracking = st.checkbox("Period Tracking")
    waterproof = st.checkbox("Waterproof")

with col6:
    amoled = st.checkbox("AMOLED")
    bluetooth = st.checkbox("Bluetooth")
    sports_modes = st.checkbox("Sports Modes")
    touchscreen = st.checkbox("Touchscreen")

# -------------------------
# PREPARE INPUT
# -------------------------
brand = reverse_map[brand_name]

input_data = pd.DataFrame([{
    'brand': brand,
    'rating': rating,
    'display_size': display_size,
    'battery_days': battery_days,
    'calling': int(calling),
    'heart_monitor': int(heart_monitor),
    'sleep_tracking': int(sleep_tracking),
    'calories': int(calories),
    'step_counter': int(step_counter),
    'period_tracking': int(period_tracking),
    'waterproof': int(waterproof),
    'amoled': int(amoled),
    'bluetooth': int(bluetooth),
    'sports_modes': int(sports_modes),
    'touchscreen': int(touchscreen)
}])

# -------------------------
# PREDICTION
# -------------------------
st.markdown("---")

if st.button("🔮 Predict Price"):
    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Price: ₹ {int(prediction)}")
    st.info(f"📊 Range: ₹ {int(prediction-300)} - ₹ {int(prediction+300)}")

# =========================
# 📊 EDA SECTION
# =========================
st.markdown("---")
st.header("📊 Data Analysis")

# -------- HEATMAP --------
st.subheader("🔥 Correlation Heatmap")

corr = df.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    annot_kws={"size":7}
)
st.pyplot(fig)

# -------- FEATURE ANALYSIS --------
st.subheader("📈 Feature vs Price")

feature = st.selectbox(
    "Select Feature",
    [
        'rating','display_size','battery_days','brand',
        'calling','heart_monitor','sleep_tracking','calories',
        'step_counter','period_tracking','waterproof',
        'amoled','bluetooth','sports_modes','touchscreen'
    ]
)

fig2, ax2 = plt.subplots()

if df[feature].nunique() <= 5:
    sns.boxplot(x=df[feature], y=df['price'], ax=ax2)
else:
    sns.scatterplot(x=df[feature], y=df['price'], ax=ax2)

ax2.set_title(f"{feature} vs Price")
st.pyplot(fig2)

# -------- PRICE DISTRIBUTION --------
st.subheader("💰 Price Distribution")

fig3, ax3 = plt.subplots()
sns.histplot(df['price'], kde=True, ax=ax3)
st.pyplot(fig3)

# -------- DATA PREVIEW --------
with st.expander("📋 Show Dataset"):
    st.dataframe(df.head(50))