import os
import shutil
import streamlit as st

from chatbot.pdf_loader import load_pdf
from chatbot.text_splitter import split_text
from chatbot.vector_store import create_vector_store
from chatbot.rag import ask_pdf


def show():

    st.title("📄 Chat with PDF")
    st.caption("Upload a PDF and ask questions based on its content.")

    if "pdf_messages" not in st.session_state:
        st.session_state["pdf_messages"] = []

    if "kb_ready" not in st.session_state:
        st.session_state["kb_ready"] = False

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        key="pdf_chat"
    )

    pdf_path = None

    if uploaded_pdf is not None:

        pdf_path = f"uploads/{uploaded_pdf.name}"

        with open(pdf_path, "wb") as file:
            file.write(uploaded_pdf.getbuffer())

        col1, col2 = st.columns(2)

        with col1:

            if st.button("📚 Build Knowledge Base", use_container_width=True):

                with st.spinner("Reading PDF..."):

                    text = load_pdf(pdf_path)
                    chunks = split_text(text)
                    create_vector_store(chunks)

                st.session_state["kb_ready"] = True
                st.success("Knowledge Base Created Successfully!")

        with col2:

            if st.button("🗑 Delete PDF", use_container_width=True):

                if os.path.exists(pdf_path):
                    os.remove(pdf_path)

                if os.path.exists("vector_db"):
                    shutil.rmtree("vector_db")
                    os.makedirs("vector_db")

                st.session_state["kb_ready"] = False
                st.session_state["pdf_messages"] = []

                st.success("PDF and Knowledge Base Deleted.")

    st.divider()

    for message in st.session_state["pdf_messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if st.session_state["kb_ready"]:

        question = st.chat_input("Ask something from the uploaded PDF...")

        if question:

            st.session_state["pdf_messages"].append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.chat_message("user"):
                st.markdown(question)

            with st.chat_message("assistant"):

                with st.spinner("Thinking..."):
                    answer = ask_pdf(question)

                st.markdown(answer)

            st.session_state["pdf_messages"].append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

    else:

        st.info("📄 Upload a PDF and build the Knowledge Base to start chatting.")