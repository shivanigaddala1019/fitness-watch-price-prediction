import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Fitness Watch Price Predictor", layout="centered")

st.title("⌚ Fitness Watch Price Predictor")
st.write("Enter specifications to predict price")

# -------------------------
# LOAD MODEL (SAFE PATH)
# -------------------------
model_path = os.path.join(os.path.dirname(__file__), "..", "model.pkl")

try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# -------------------------
# INPUTS
# -------------------------
brand = st.selectbox("Brand", [0,1,2,3,4])
rating = st.slider("Rating", 0.0, 5.0, 3.5)
display = st.number_input("Display Size (inches)", 1.0, 50.0, 1.8)
battery = st.slider("Battery Days", 1, 15, 7)

calling = st.selectbox("Bluetooth Calling", [0,1])
heart = st.selectbox("Heart Monitor", [0,1])
sleep = st.selectbox("Sleep Tracking", [0,1])
calories = st.selectbox("Calories Tracking", [0,1])
step = st.selectbox("Step Counter", [0,1])
period = st.selectbox("Period Tracking", [0,1])
waterproof = st.selectbox("Waterproof", [0,1])

amoled = st.selectbox("AMOLED Display", [0,1])
bluetooth = st.selectbox("Bluetooth", [0,1])
sports = st.selectbox("Sports Modes", [0,1])
touch = st.selectbox("Touchscreen", [0,1])

# -------------------------
# PREDICT
# -------------------------
if st.button("Predict Price 💰"):

    input_data = pd.DataFrame([[
        brand, rating, display, battery,
        calling, heart, sleep, calories,
        step, period, waterproof,
        amoled, bluetooth, sports, touch
    ]], columns=[
        'brand','rating','display_size','battery_days',
        'calling','heart_monitor','sleep_tracking','calories',
        'step_counter','period_tracking','waterproof',
        'amoled','bluetooth','sports_modes','touchscreen'
    ])

    price = model.predict(input_data)[0]

    st.success(f"💰 Estimated Price: ₹ {int(price)}")
    st.info(f"📊 Range: ₹ {int(price-300)} - ₹ {int(price+300)}")