from chatbot.vector_store import (
    load_vector_store,
    get_embedding,
)
from chatbot.groq_client import generate_response


def retrieve_context(query: str, top_k: int = 3):
    """
    Retrieve the most relevant text chunks from FAISS.
    """

    index, chunks = load_vector_store()

    query_embedding = get_embedding(query)

    _, indices = index.search(query_embedding, top_k)

    context = []

    for idx in indices[0]:
        if 0 <= idx < len(chunks):
            context.append(chunks[idx])

    return "\n\n".join(context)


def ask_pdf(question: str):
    """
    Ask a question using retrieved PDF context.
    """

    context = retrieve_context(question)

    prompt = f"""
Use ONLY the context below to answer the user's question.

If the answer is not present in the context, reply:
"I couldn't find the answer in the uploaded PDF."

Context:
{context}

Question:
{question}
"""

    return generate_response(prompt)