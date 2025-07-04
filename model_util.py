import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def ask_claude(question, dataset_text):
    messages = [
        {"role": "system", "content": "You are an IPL cricket expert. Use the given data to answer the question only answer not steps or explantion."},
        {"role": "user", "content": f"DATA:\n{dataset_text}\n\nQUESTION:\n{question}"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="deepseek/deepseek-chat",
            messages=messages
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Claude API error: {e}"
