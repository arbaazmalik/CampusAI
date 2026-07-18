import json
import os

from groq import Groq
from dotenv import load_dotenv

from utils.constants import MODEL_NAME
from chatbot.prompts import SYSTEM_PROMPT, MCQ_PROMPT

# Load environment variables
load_dotenv()

# Read API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Please add it to your .env file."
    )

# Initialize Groq Client
client = Groq(api_key=GROQ_API_KEY)


def generate_response(user_prompt: str) -> str:
    """
    Generate an AI response using Groq.
    """

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.3,
            max_tokens=4096,
            top_p=1,
            stream=False,
        )

        return completion.choices[0].message.content.strip()

    except Exception as error:
        return f"Error: {str(error)}"


import json


def generate_mcqs(content: str, num_questions: int = 10):

    prompt = MCQ_PROMPT.format(
        content=content,
        num_questions=num_questions
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=2000
    )

    text = response.choices[0].message.content.strip()

    # Remove markdown if model adds it
    text = text.replace("```json", "").replace("```", "").strip()

    try:
     return json.loads(text)

    except Exception as e:
     print("\n========== RAW GROQ RESPONSE ==========\n")
     print(text)
     print("\n=======================================\n")
     raise e