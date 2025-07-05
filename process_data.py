# process_data.py

import pandas as pd
import re

# Load IPL dataset
df = pd.read_csv("matches.csv")

# Extract year from the question
def extract_year(text):
    match = re.search(r"(20\d{2})", text)
    return int(match.group(1)) if match else None

# Filter dataset based on year 
def get_filtered_data(message):
    year = extract_year(message)
    if year:
        filtered = df[df["season"] == year]
        if not filtered.empty:
            return filtered.to_string(index=False), f"✅ Showing data for question: {message}"
        else:
            return df.head(30).to_string(index=False), f"⚠️ No data for {year}, showing first 30 rows."
    else:
        return df.head(30).to_string(index=False), "ℹ️ No year found, showing first 30 rows."

# Optionally export full dataset (for no-filter use)
def get_full_data():
    return df.to_string(index=False)
