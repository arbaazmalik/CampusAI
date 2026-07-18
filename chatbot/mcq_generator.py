from chatbot.pdf_loader import load_pdf
from chatbot.groq_client import generate_mcqs


def generate_mcq_from_pdf(pdf_path: str, num_questions: int = 10):

    text = load_pdf(pdf_path)

    mcqs = generate_mcqs(
        content=text,
        num_questions=num_questions
    )

    return mcqs