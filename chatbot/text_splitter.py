from langchain_text_splitters import RecursiveCharacterTextSplitter

from utils.constants import CHUNK_SIZE, CHUNK_OVERLAP


def split_text(text: str):
    """
    Split extracted text into smaller chunks for RAG.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    return splitter.split_text(text)