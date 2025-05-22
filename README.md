# 🤖 DAO Worker AI Agent (Aptos x GCP Hackathon Project)

A smart AI-powered agent that assists DAOs by summarizing lengthy proposals and submitting them on-chain for better transparency, faster decision-making, and efficient task handling.

---

## 📌 Project Overview

This app allows DAO users to:
- 📝 Submit a DAO proposal text.
- 🤖 Get a summarized version using an AI Agent.
- 🔗 Submit both original and summarized proposals on-chain (mocked in this version).
- 💾 Save task logs for future audit.

---

## 🏗️ Project Structure

```bash
dao-worker-ai-agent/
│
├── backend/                   # Flask Backend AI Agent
│   ├── app.py                 # Main Flask app
│   ├── ai_agent.py            # AI logic (summarization)
│   ├── blockchain.py          # Simulated blockchain interaction
│   ├── config.py              # API keys, contract address config
│   ├── tasks.db               # SQLite DB (optional, unused now)
│   └── requirements.txt       # Python dependencies
│
├── templates/                 # Jinja2 HTML Templates
│   └── index.html             # Main UI
│
├── static/                    # Static frontend files
│   ├── task.js                # JS to submit tasks via AJAX
│   └── styles.css             # Optional styling
│
├── contracts/                 # Smart Contracts
│   ├── DAOAgent.sol           # Solidity contract (with ProposalSummary event)
│   ├── deploy.js              # Deployment script using Hardhat
│   └── hardhat.config.js      # Hardhat config
│
├── saved/                     # Task logs folder (auto saved)
│   └── summary_*.json         # Stored AI summaries
│
├── .env                       # Secret environment variables
├── run.sh                     # Optional unified run script
└── README.md                  # This file
````

---

## ⚙️ Setup Instructions

### 1. 📦 Install Backend Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 🔐 Set Environment Variables

Create `.env` file in the root:

```
OPENAI_API_KEY=your_openai_key
PRIVATE_KEY=your_eth_private_key
CONTRACT_ADDRESS=0xYourSmartContractAddress
```

> ⚠️ For now, Web3 interactions are mocked. You can integrate actual logic later.

---

## 🚀 Run the Application

```bash
cd backend
python app.py
```

Then open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Task Logic: Summarize DAO Proposals

The default agent behavior:

* Takes a full DAO proposal (any long text)
* Truncates or simulates a summary (basic logic in `ai_agent.py`)
* Submits both original and summary to mocked blockchain
* Returns a mock transaction hash

To replace it with real AI:

```python
# In ai_agent.py
import openai
openai.api_key = config.OPENAI_API_KEY

def handle_task(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following proposal:\n{prompt}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
```

---

## 💡 How to Modify or Extend

| Feature                         | File(s) to Edit                | What to Do                           |
| ------------------------------- | ------------------------------ | ------------------------------------ |
| Replace summary logic with AI21 | `backend/ai_agent.py`          | Use AI21's API with your key         |
| Connect to real contract        | `backend/blockchain.py`        | Use Web3.py to send tx               |
| Add proposal history page       | `backend/app.py`, `index.html` | Query saved JSON and render table    |
| Deploy smart contract           | `contracts/DAOAgent.sol`       | Use Hardhat & deploy.js              |
| Style app UI                    | `static/styles.css`            | Add Bootstrap classes or custom CSS  |
| Deploy to web                   | `run.sh`, `app.py`             | Use Gunicorn + Nginx or `render.com` |

---

## 📦 requirements.txt

```txt
Flask
Flask-Cors
python-dotenv
openai
web3
```

---

## 👨‍💻 Example Smart Contract Usage

```solidity
event ProposalSummary(string original, string summary);

function submitSummary(string memory original, string memory summary) public {
    emit ProposalSummary(original, summary);
}
```

---

## 🏁 Hackathon Theme Alignment

* ✅ AI summarization of DAO tasks
* ✅ Smart contract event logging
* ✅ Bootstrap + Flask simplicity
* ✅ Designed to run even with low resources

---

## 🤝 Contributing

Pull requests and forks are welcome. This project is part of the **Aptos x GCP Hackathon**, and all contributions must follow ethical and open standards.

---

## 🧪 Future Upgrades

* Smart contract voting & staking
* GPT-4 agent with task classification
* Save all tasks in SQLite DB
* Multi-agent collaboration

---

