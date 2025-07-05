from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- import CORS
from process_data import get_filtered_data, get_full_data
from model_util import ask
import os
app = Flask(__name__)

CORS(app, origins=["https://ibm-project-frontend-beta.vercel.app/"])

@app.route("/ask", methods=["GET", "POST"])
def handle_question():
    if request.method == "GET":
        question = request.args.get("question")
    else:
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
    return jsonify({
        "welcome": "Welcome to the IPL Cricket Expert API! Ask your questions about IPL matches.",
        "link": "https://boundrybot.onrender.com/ask?question=list%20of%20teams%20in%202012"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
