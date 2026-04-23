from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

all_data = []

search_queries = [
    "smartwatch",
    "fitness watch",
    "women smartwatch",
    "smartwatch women",
    "fitness band watch"
]

for query in search_queries:
    print(f"\n🔍 Searching: {query}")

    for page in range(1, 7):   # ~400 products

        url = f"https://www.flipkart.com/search?q={query}&page={page}"
        driver.get(url)

        time.sleep(5)

        # Close popup
        try:
            driver.execute_script(
                "document.querySelector('button._2KpZ6l._2doB4z')?.click()"
            )
        except:
            pass

        time.sleep(2)

        # 🔥 JS scraping + feature extraction
        data = driver.execute_script("""
        let items = document.querySelectorAll('[data-id]');
        let result = [];

        items.forEach(item => {

            let text = item.innerText.toLowerCase();

            let title = text.split('\\n')[0];

            let price = text.match(/₹[0-9,]+/);
            let rating = text.match(/\\d\\.\\d/);

            let img = item.querySelector('img');
            let img_url = img ? img.src : "";

            // 🔥 FEATURE EXTRACTION (YES / NO)
            let heart = (text.includes("heart") || text.includes("hr")) ? "Yes" : "No";
            let sleep = text.includes("sleep") ? "Yes" : "No";
            let calories = text.includes("calorie") ? "Yes" : "No";
            let calling = text.includes("calling") ? "Yes" : "No";
            let step = text.includes("step") ? "Yes" : "No";
            let period = text.includes("period") ? "Yes" : "No";
            let waterproof = (text.includes("water") || text.includes("ip67") || text.includes("ip68")) ? "Yes" : "No";

            if(title && price){
                result.push({
                    title: title,
                    price: price ? price[0] : "0",
                    rating: rating ? rating[0] : "0",
                    image: img_url,

                    heart_monitor: heart,
                    sleep_tracking: sleep,
                    calories: calories,
                    calling: calling,
                    step_counter: step,
                    period_tracking: period,
                    waterproof: waterproof
                });
            }
        });

        return result;
        """)

        print(f"{query} - Page {page}: {len(data)}")

        all_data.extend(data)

driver.quit()

# -----------------------------
# Convert to DataFrame
# -----------------------------
df = pd.DataFrame(all_data)

# Remove duplicates
df = df.drop_duplicates()

# Save CSV
df.to_csv("flipkart_data.csv", index=False)

print("\n✅ FINAL SCRAPING DONE!")
print("Total products:", len(df))