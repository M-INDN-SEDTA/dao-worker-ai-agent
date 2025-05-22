# backend/ai_agent.py

def handle_task(prompt: str) -> str:
    # Simulated AI summary
    summary = prompt[:75] + "..." if len(prompt) > 75 else prompt
    return f"Summary: {summary}"

# import openai
# openai.api_key = config.OPENAI_API_KEY
# 
# def handle_task(prompt: str) -> str:
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=f"Summarize this DAO proposal:\n{prompt}",
#         max_tokens=100
#     )
#     return response.choices[0].text.strip()
