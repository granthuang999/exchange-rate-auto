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

# Create README content line by line
readme_lines = []
readme_lines.append("# Exchange Rates Auto Update")
readme_lines.append("")
readme_lines.append("## Latest Data")
readme_lines.append("")
readme_lines.append("Updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
readme_lines.append("")
readme_lines.append("### For Excel (copy and paste):")
readme_lines.append("")
readme_lines.append("```
readme_lines.append("Currency\tCNY\tHKD\tUSD\tEUR\tGBP")
readme_lines.append("CNY\t\t1.0989\t0.1392\t0.1198\t0.1039")
readme_lines.append("HKD\t0.9100\t\t0.1267\t0.1090\t0.0946")
readme_lines.append("USD\t7.1860\t7.8945\t\t0.8577\t0.7460")
readme_lines.append("EUR\t8.3430\t9.1703\t1.1660\t\t0.8700")
readme_lines.append("GBP\t9.6250\t10.5769\t1.3404\t1.1494\t")
readme_lines.append("```")
readme_lines.append("")
readme_lines.append("### CSV Link:")
readme_lines.append("https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv")
readme_lines.append("")
readme_lines.append("### Instructions:")
readme_lines.append("1. Copy the table above and paste into Excel")
readme_lines.append("2. Or use the CSV link in Excel Data > Get Data > From Web")
readme_lines.append("")
readme_lines.append("---")
readme_lines.append("*Data for reference only*")

readme_content = "\n".join(readme_lines)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
print("README updated")

print("All files updated successfully!")
