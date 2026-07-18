from chatbot.pdf_loader import load_pdf
from chatbot.groq_client import generate_response


def generate_viva_questions(pdf_path: str, num_questions: int = 10):

    text = load_pdf(pdf_path)

    prompt = f"""
You are a university viva examiner.

Read the study material carefully.

Generate exactly {num_questions} viva questions.

For EVERY question, immediately provide its answer.

Follow this format exactly:

## Question 1
What is Artificial Intelligence?

### Answer
Artificial Intelligence is the simulation of human intelligence by machines.

----------------------------------------

## Question 2
What is Machine Learning?

### Answer
Machine Learning is a subset of Artificial Intelligence that enables computers to learn from data.

----------------------------------------

Rules:
- Every question MUST have an answer.
- Never skip the answer.
- Do not write introductory text.
- Do not write concluding text.
- Keep answers between 3–8 lines.
- Use only the given study material.

Study Material:

{text}
"""

    return generate_response(prompt)