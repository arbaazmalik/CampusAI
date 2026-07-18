import re


def extract_mcqs(text: str):
    """
    Convert LLM MCQ response into structured data.
    """

    questions = []

    blocks = re.split(r"\n\s*\n", text.strip())

    for block in blocks:

        lines = [line.strip() for line in block.split("\n") if line.strip()]

        if len(lines) < 6:
            continue

        question = lines[0]

        options = lines[1:5]

        answer = ""

        for line in lines:
            if "correct" in line.lower():
                answer = line.split(":")[-1].strip()

        questions.append(
            {
                "question": question,
                "options": options,
                "answer": answer
            }
        )

    return questions