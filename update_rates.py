import pandas as pd
from datetime import datetime
import json

print("Starting update...")

# Exchange rates data
data = [
    ["Currency", "CNY", "HKD", "USD", "EUR", "GBP"],
    ["CNY", "", "1.0989", "0.1392", "0.1198", "0.1039"],
    ["HKD", "0.9100", "", "0.1267", "0.1090", "0.0946"], 
    ["USD", "7.1860", "7.8945", "", "0.8577", "0.7460"],
    ["EUR", "8.3430", "9.1703", "1.1660", "", "0.8700"],
    ["GBP", "9.6250", "10.5769", "1.3404", "1.1494", ""]
]

# Save CSV
df = pd.DataFrame(data[1:], columns=data[0])
df.to_csv("exchange_rates.csv", index=False)
print("CSV saved")

# Save JSON  
rates_data = {
    "USD_CNY": 7.1860,
    "EUR_CNY": 8.3430,
    "GBP_CNY": 9.6250,
    "HKD_CNY": 0.9100,
    "last_updated": datetime.now().isoformat()
}

with open("exchange_rates.json", "w") as f:
    json.dump(rates_data, f, indent=2)
print("JSON saved")

# Create README
readme_text = """# Exchange Rates Auto Update

## Latest Data

Updated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """

### For Excel (copy and paste):

