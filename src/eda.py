import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style
sns.set_style("whitegrid")

def run_eda():
    df = pd.read_csv("data/cleaned_data.csv")

    print("\n📊 DATA OVERVIEW")
    print(df.head())

    print("\n📌 SHAPE:", df.shape)

    print("\n📌 COLUMNS")
    print(df.columns)

    # =========================
    # 🎯 1. PRICE DISTRIBUTION
    # =========================
    plt.figure(figsize=(8,5))
    sns.histplot(df['price'], kde=True)
    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    # =========================
    # 🎯 2. NUMERIC RELATIONSHIPS
    # =========================
    fig, axes = plt.subplots(1, 2, figsize=(12,5))

    sns.scatterplot(x=df['rating'], y=df['price'], ax=axes[0])
    axes[0].set_title("Rating vs Price")

    sns.scatterplot(x=df['display_size'], y=df['price'], ax=axes[1])
    axes[1].set_title("Display Size vs Price")

    plt.tight_layout()
    plt.show()

    # =========================
    # 🎯 3. BRAND ANALYSIS
    # =========================
    plt.figure(figsize=(8,5))
    sns.boxplot(x=df['brand'], y=df['price'])
    plt.title("Brand vs Price")
    plt.tight_layout()
    plt.show()

    # =========================
    # 🎯 4. FEATURE IMPACT
    # =========================
    features = [
        'calling','heart_monitor','sleep_tracking',
        'waterproof','amoled','bluetooth',
        'sports_modes','touchscreen'
    ]

    fig, axes = plt.subplots(2, 4, figsize=(16,8))

    for i, f in enumerate(features):
        sns.boxplot(x=df[f], y=df['price'], ax=axes[i//4, i%4])
        axes[i//4, i%4].set_title(f"{f} vs Price")

    plt.tight_layout()
    plt.show()

    # =========================
    # 🎯 5. HEATMAP (WITH VALUES)
    # =========================
    plt.figure(figsize=(14,10))

    corr = df.corr(numeric_only=True)

    sns.heatmap(
        corr,
        annot=True,             # ✅ SHOW VALUES
        fmt=".2f",              # ✅ 2 decimal precision
        cmap="coolwarm",
        square=True,            # ✅ neat grid
        linewidths=0.5,
        annot_kws={"size":7}    # ✅ smaller text (no overlap)
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_eda()