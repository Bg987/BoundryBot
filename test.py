# test.py

from process_data import get_filtered_data, get_full_data
from model_util import ask

question = input("❓ Enter your IPL question: ")

#acccess full dataset
# data_to_send = get_full_data()

# Option 2: Use filtered dataset based on year
data_to_send, info = get_filtered_data(question)

print("🔎", info)

# Ask the model
response = ask(question, data_to_send)

print("\n📤 Answer:\n", response)
