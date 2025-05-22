# Simulated blockchain interaction (replace with web3.py in real use)

# Dummy tasks store
_tasks = [
    {"task_id": 1, "description": "Research new blockchain scalability solutions."},
    {"task_id": 2, "description": "Write documentation for DAO voting system."}
]

# Dummy summaries store
_summaries = {}

def get_tasks_from_chain():
    # Normally, read from smart contract using web3.py
    return _tasks

def submit_summary_to_chain(task_id, summary):
    # Normally, write summary back to smart contract
    _summaries[task_id] = summary
    print(f"Submitted summary for task {task_id} to blockchain (simulated).")
