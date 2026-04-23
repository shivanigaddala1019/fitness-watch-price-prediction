import pandas as pd
import re

def clean_data():
    df = pd.read_csv("data/flipkart_data.csv")

    df.columns = df.columns.str.strip().str.lower()

    # ----------------------------
    # CLEAN PRICE
    # ----------------------------
    df['price'] = df['price'].str.replace('₹','').str.replace(',','')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # ----------------------------
    # CLEAN RATING
    # ----------------------------
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0)

    # ----------------------------
    # FEATURE EXTRACTION FROM TITLE
    # ----------------------------
    def extract_feature(text, keyword):
        return 1 if keyword in text.lower() else 0

    df['calling'] = df['title'].apply(lambda x: extract_feature(x, "calling"))
    df['heart_monitor'] = df['title'].apply(lambda x: extract_feature(x, "heart"))
    df['sleep_tracking'] = df['title'].apply(lambda x: extract_feature(x, "sleep"))
    df['calories'] = df['title'].apply(lambda x: extract_feature(x, "calorie"))
    df['step_counter'] = df['title'].apply(lambda x: extract_feature(x, "step"))
    df['period_tracking'] = df['title'].apply(lambda x: extract_feature(x, "period"))
    df['waterproof'] = df['title'].apply(lambda x: extract_feature(x, "water"))
    
    # 🔥 NEW FEATURES
    df['amoled'] = df['title'].apply(lambda x: extract_feature(x, "amoled"))
    df['bluetooth'] = df['title'].apply(lambda x: extract_feature(x, "bluetooth"))
    df['sports_modes'] = df['title'].apply(lambda x: extract_feature(x, "sports"))
    df['touchscreen'] = df['title'].apply(lambda x: extract_feature(x, "touch"))

    # ----------------------------
    # BRAND ENCODING
    # ----------------------------
    def get_brand(title):
        title = title.lower()
        if "noise" in title: return 1
        elif "boat" in title: return 2
        elif "fire-boltt" in title: return 3
        elif "fastrack" in title: return 4
        else: return 0

    df['brand'] = df['title'].apply(get_brand)

    # ----------------------------
    # DISPLAY SIZE
    # ----------------------------
    def extract_display(text):
        match = re.search(r'(\d+(\.\d+)?)\s*(inch|mm)', text.lower())
        return float(match.group(1)) if match else 1.8

    df['display_size'] = df['title'].apply(extract_display)

    # ----------------------------
    # BATTERY
    # ----------------------------
    def extract_battery(text):
        match = re.search(r'(\d+)\s*day', text.lower())
        return int(match.group(1)) if match else 7

    df['battery_days'] = df['title'].apply(extract_battery)

    # ----------------------------
    # DROP NULLS
    # ----------------------------
    df = df.dropna()

    # ----------------------------
    # REMOVE OUTLIERS
    # ----------------------------
    df = df[df['price'] < 15000]

    df.to_csv("data/cleaned_data.csv", index=False)

    print("✅ CLEANED DATA SAVED")

if __name__ == "__main__":
    clean_data()