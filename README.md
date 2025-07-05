# BoundryBot🏏 BoundaryBot - IPL Q&A AI Assistant
====================================

BoundaryBot is an intelligent question-answering service designed to answer questions about the Indian Premier League (IPL) using a real historical dataset. It uses a language model to interpret user queries and provide meaningful responses based on IPL match data from 2008 to 2023.

It can answer questions like:
- "Who won the IPL in 2023?"
- "Which team had the most wins in 2016?"
- "Who was the player of the match in the 2019 final?"
- "How many matches were decided by super over in 2020?"

------------------------------------
🔧 Key Features
------------------------------------
- ✅ Context-aware Q&A powered by a language model
- ✅ Reads and filters data from a structured IPL dataset (`matches.csv`)
- ✅ Filters data year-wise to manage token limits effectively
- ✅ Flask-based backend with clean API routes
- ✅ Supports both JSON body and URL query for questions
- ✅ Environment variables securely manage API keys

------------------------------------
🧠 Technologies Used
------------------------------------
- Python (core programming language)
- Flask (web framework)
- Pandas (data processing)
- Cohere API 

------------------------------------
📦 Project Structure Overview
------------------------------------
- server.py         → Flask app with `/ask` endpoint
- process_data.py   → Handles IPL dataset loading & filtering
- model_util.py     → Interfaces with LLM API to generate responses
- matches.csv       → IPL dataset used for answering questions
- .env              → Stores API key (not pushed to Git)
- req.txt  → Python dependencies
- .gitignore        → Ignores cache, env files, and logs

------------------------------------
📌 Note
------------------------------------
- The `.env` file is excluded from version control for security and contains the required API key.
- The project uses a static dataset (`matches.csv`) covering IPL data from 2008 to 2023.

