from flask import Flask, render_template, request, jsonify
from rag_engine import EnterpriseBrain
import os

app = Flask(__name__)
brain = EnterpriseBrain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        path = os.path.join("uploads", file.filename)
        file.save(path)
        status = brain.process_pdf(path)
        return jsonify({"status": status})

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("question")
    response = brain.ask_question(user_input)
    return jsonify({"answer": response})

if __name__ == '__main__':
    if not os.path.exists("uploads"): os.makedirs("uploads")
    app.run(debug=True)