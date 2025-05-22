# backend/app.py
from flask import Flask, render_template, request, jsonify
from backend.ai_agent import handle_task
from backend.blockchain import submit_result_to_chain
import os
import json, time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_task', methods=['POST'])
def submit_task():
    data = request.json
    task_input = data.get("task")
    ai_result = handle_task(task_input)
    tx_hash = submit_result_to_chain(task_input, ai_result)
    return jsonify({"result": ai_result, "tx_hash": tx_hash})


def save_task(task, summary):
    ts = int(time.time())
    with open(f"saved/summary_{ts}.json", "w") as f:
        json.dump({"task": task, "summary": summary}, f)