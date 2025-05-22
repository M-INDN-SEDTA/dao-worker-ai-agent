from flask import Flask, render_template, request, jsonify
from backend.ai_agent import summarize_task
from backend.blockchain import get_tasks_from_chain, submit_summary_to_chain
from backend.config import load_env
import os
import json
import datetime

app = Flask(__name__, template_folder="../templates", static_folder="../static")

load_env()

# In-memory task summaries cache
summaries = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    # Get tasks from blockchain (simulated here)
    tasks = get_tasks_from_chain()
    return jsonify(tasks)

@app.route("/api/submit_summary", methods=["POST"])
def submit_summary():
    data = request.json
    task_id = data.get("task_id")
    description = data.get("description")
    if not task_id or not description:
        return jsonify({"error": "Missing task_id or description"}), 400

    summary = summarize_task(description)

    # Save summary to JSON file
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"summary_{task_id}_{timestamp}.json"
    path = os.path.join("saved", filename)
    os.makedirs("saved", exist_ok=True)
    with open(path, "w") as f:
        json.dump({"task_id": task_id, "summary": summary}, f, indent=4)

    # Submit summary to blockchain (simulated)
    submit_summary_to_chain(task_id, summary)

    # Cache summary
    summaries.append({"task_id": task_id, "summary": summary})

    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(debug=True)
