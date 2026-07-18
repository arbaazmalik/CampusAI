import os
import pickle

import faiss
from sentence_transformers import SentenceTransformer

from utils.constants import (
    EMBEDDING_MODEL,
    VECTOR_DB_FOLDER,
)

# Load embedding model
embedding_model = SentenceTransformer(EMBEDDING_MODEL)


def create_vector_store(chunks):
    """
    Create and save FAISS vector database.
    """

    embeddings = embedding_model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    os.makedirs(VECTOR_DB_FOLDER, exist_ok=True)

    faiss.write_index(
        index,
        os.path.join(VECTOR_DB_FOLDER, "faiss_index.bin")
    )

    with open(
        os.path.join(VECTOR_DB_FOLDER, "chunks.pkl"),
        "wb"
    ) as file:
        pickle.dump(chunks, file)


def load_vector_store():
    """
    Load saved FAISS vector database.
    """

    index = faiss.read_index(
        os.path.join(VECTOR_DB_FOLDER, "faiss_index.bin")
    )

    with open(
        os.path.join(VECTOR_DB_FOLDER, "chunks.pkl"),
        "rb"
    ) as file:
        chunks = pickle.load(file)

    return index, chunks


def get_embedding(text):
    """
    Convert text into embedding.
    """

    return embedding_model.encode([text])