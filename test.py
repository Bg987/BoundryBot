import pandas as pd
import re
from model_util import ask_claude

# Load IPL data
df = pd.read_csv("cricket_data.csv")

#get year from question
def extract_year(text):
    match = re.search(r"(20\d{2})", text)
    return int(match.group(1)) if match else None

#filter data based on year extracted from the question due to limit of token limit
def get_filtered_data(message):
    year = extract_year(message)
    if year:
        filtered = df[df["season"] == year]
        if not filtered.empty:
            return filtered.to_string(index=False), f"✅ Showing data for question {message}"
        else:
            return df.head(30).to_string(index=False), f"⚠️ No data for {year}, showing"
    else:
        return df.head(30).to_string(index=False), "ℹ️ No year found."

question = input("❓ Enter your IPL question for specific year : ")

# Filter data + ask Claude
filtered_data, info = get_filtered_data(question)
print("🔎", info)
response = ask_claude(question, filtered_data)

print("\n🤖 Claude's answer:\n", response)
