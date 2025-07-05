
from flask import Flask, request, jsonify
from process_data import get_filtered_data, get_full_data
from model_util import ask
import os
app = Flask(__name__)

@app.route("/ask", methods=["GET", "POST"])
def handle_question():
    # Allow question via query param (GET)
    if request.method == "GET":
        question = request.args.get("question")
    else:
        # For POST requests (JSON body)
        data = request.get_json()
        question = data.get("question") if data else None

    if not question:
        return jsonify({"error": "Missing 'question'"}), 400

    dataset_text, info = get_filtered_data(question)
    answer = ask(question, dataset_text)

    return jsonify({
        "info": info,
        "answer": answer
    })

@app.route("/", methods=["GET"])
def root():
    return "🏏 IPL Q&A API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

