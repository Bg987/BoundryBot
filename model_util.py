import cohere
import os
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def ask(question, dataset_text):
    prompt = (
        "You are an IPL cricket expert. "
        "Answer only based on the data below. Give only answer .\n\n"
        f"DATA:\n{dataset_text}\n\n"
        f"QUESTION:\n{question}"
    )

    try:
        response = co.generate(
            model="command-r-plus",  # Or "command-r"
            prompt=prompt,
            max_tokens=300,
            temperature=0.5,
            stop_sequences=["\n\n"]
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"⚠️ Cohere API error: {e}"
