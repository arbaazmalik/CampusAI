import os
import pickle
import streamlit as st

import faiss
from sentence_transformers import SentenceTransformer

from utils.constants import (
    EMBEDDING_MODEL,
    VECTOR_DB_FOLDER,
)


@st.cache_resource
def get_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL)


def create_vector_store(chunks):
    """
    Create and save FAISS vector database.
    """

    embedding_model = get_embedding_model()

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

    embedding_model = get_embedding_model()

    return embedding_model.encode([text])