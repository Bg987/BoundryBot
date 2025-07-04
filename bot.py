import os
import re
import pandas as pd
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from model_util import ask_claude

load_dotenv()

df = pd.read_csv("Cricket_data.csv")

def extract_year(text):
    match = re.search(r"(20\d{2})", text)
    return int(match.group(1)) if match else None

def get_filtered_data(user_msg):
    year = extract_year(user_msg)
    if year:
        filtered = df[df["season"] == year]
        if not filtered.empty:
            return filtered.to_string(index=False), f"✅ IPL {year} data filtered"
        else:
            return df.head(30).to_string(index=False), f"⚠️ No data for {year}, showing sample"
    else:
        return df.head(30).to_string(index=False), "ℹ️ No year found, using sample"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏏 Welcome to the IPL Q&A Bot!\nAsk me questions like:\n- Top scorer in 2023\n- Who won IPL 2022?"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    filtered_data, info = get_filtered_data(user_msg)
    await update.message.reply_text(f"{info} — asking Claude... ⏳")

    answer = ask_claude(user_msg, filtered_data)
    await update.message.reply_text(answer)

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
