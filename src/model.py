import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Models
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR

# Optional models
try:
    from xgboost import XGBRegressor
except:
    XGBRegressor = None

try:
    from lightgbm import LGBMRegressor
except:
    LGBMRegressor = None

try:
    from catboost import CatBoostRegressor
except:
    CatBoostRegressor = None


def train_models():
    df = pd.read_csv("data/cleaned_data.csv")

    # -------------------------
    # FEATURES
    # -------------------------
    features = [
        'brand','rating','display_size','battery_days',
        'calling','heart_monitor','sleep_tracking','calories',
        'step_counter','period_tracking','waterproof',
        'amoled','bluetooth','sports_modes','touchscreen'
    ]

    X = df[features]
    y = df['price']

    # -------------------------
    # SPLIT DATA
    # -------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -------------------------
    # MODELS
    # -------------------------
    models = {
        "Linear Regression": LinearRegression(),
        "Ridge": Ridge(),
        "Lasso": Lasso(),
        "Random Forest": RandomForestRegressor(n_estimators=150),
        "Gradient Boosting": GradientBoostingRegressor(),
        "KNN": KNeighborsRegressor(),
        "SVR": SVR()
    }

    # Optional advanced models
    if XGBRegressor:
        models["XGBoost"] = XGBRegressor(n_estimators=200)

    if LGBMRegressor:
        models["LightGBM"] = LGBMRegressor()

    if CatBoostRegressor:
        models["CatBoost"] = CatBoostRegressor(verbose=0, iterations=200)

    print("\n📊 MODEL COMPARISON\n")

    results = []

    # -------------------------
    # TRAIN + EVALUATE
    # -------------------------
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        # MAPE (your "MARE")
        mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

        results.append((name, r2, mae, rmse, mape, model))

        print(f"🔹 {name}")
        print(f"   R²   : {r2:.3f}")
        print(f"   MAE  : {mae:.2f}")
        print(f"   RMSE : {rmse:.2f}")
        print(f"   MAPE : {mape:.2f}%")
        print("-"*40)

    # -------------------------
    # BEST MODEL SELECTION
    # -------------------------
    best = max(results, key=lambda x: x[1])

    print("\n🏆 BEST MODEL:", best[0])
    print(f"📈 R² Score: {best[1]:.3f}")
    print(f"📉 MAE: {best[2]:.2f}")
    print(f"📉 RMSE: {best[3]:.2f}")
    print(f"📉 MAPE: {best[4]:.2f}%")

    # -------------------------
    # SAVE MODEL
    # -------------------------
    joblib.dump(best[5], "model.pkl")
    print("✅ Model saved as model.pkl")


if __name__ == "__main__":
    train_models()