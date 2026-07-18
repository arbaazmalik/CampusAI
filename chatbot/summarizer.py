from chatbot.pdf_loader import load_pdf
from chatbot.groq_client import generate_response


def summarize_pdf(pdf_path: str):

    text = load_pdf(pdf_path)

    prompt = f"""
You are an expert study assistant.

Summarize the following PDF into well-structured study notes.

Requirements:

- Use proper headings.
- Use bullet points.
- Highlight important concepts.
- Keep the summary concise.
- Make it easy for revision.
- Don't miss important information.

PDF Content:

{text}
"""

    return generate_response(prompt)
