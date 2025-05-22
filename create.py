import os

# Define project root
root = "dao-worker-ai-agent"

# Define folders and files to create
structure = {
    root: [
        "run.sh",
        ".env",
        "README.md",
        ("backend", [
            "app.py",
            "ai_agent.py",
            "blockchain.py",
            "config.py",
            "tasks.db",
            "requirements.txt",
        ]),
        ("templates", [
            "index.html",
        ]),
        ("static", [
            "task.js",
            "styles.css",
        ]),
        ("contracts", [
            "DAOAgent.sol",
            "deploy.js",
            "hardhat.config.js",
        ]),
        ("saved", [
            # no files initially, just folder
        ]),
    ]
}

def create_structure(base_path, struct):
    for item in struct:
        if isinstance(item, tuple):
            # it's a folder with subitems
            folder_name, subitems = item
            folder_path = os.path.join(base_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            create_structure(folder_path, subitems)
        else:
            # it's a file
            file_path = os.path.join(base_path, item)
            # create file if doesn't exist
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    pass  # empty file

if __name__ == "__main__":
    create_structure(".", structure[root])
    print(f"Project structure created under folder '{root}'")
