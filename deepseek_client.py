# deepseek_client.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_resume_question(resume_text: str, user_question: str) -> str:
    if not API_KEY:
        raise EnvironmentError("DeepSeek API key not set. Add it to your .env file.")

    messages = [
        {"role": "system", "content": "You are a helpful assistant answering questions about resumes."},
        {"role": "user", "content": f"Here is the resume:\n\n{resume_text}\n\nNow answer this question:\n{user_question}"}
    ]

    payload = {
        "model": "deepseek-chat",  # Adjust if you're using a different DeepSeek model
        "messages": messages
    }

    response = requests.post(API_URL, json=payload, headers=HEADERS)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        raise RuntimeError(f"DeepSeek API error {response.status_code}: {response.text}")
