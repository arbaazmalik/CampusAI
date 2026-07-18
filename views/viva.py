import streamlit as st

from chatbot.viva_generator import generate_viva_questions


def show():

    st.title("🎤 Viva Question Generator")
    st.caption("Generate AI-powered viva questions and answers from your PDF.")

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        key="viva_pdf"
    )

    if uploaded_pdf is None:

        st.info("📄 Upload a PDF to generate viva questions.")
        return

    num_questions = st.slider(
        "Number of Questions",
        min_value=5,
        max_value=20,
        value=10
    )

    pdf_path = f"uploads/{uploaded_pdf.name}"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())

    if st.button("🎤 Generate Viva Questions", use_container_width=True):

        with st.spinner("Generating Viva Questions..."):

            questions = generate_viva_questions(
                pdf_path,
                num_questions
            )

        st.divider()

        st.subheader("🎓 Viva Questions & Answers")

        st.markdown(questions)

        st.download_button(
            "📥 Download Questions",
            questions,
            file_name="viva_questions.txt",
            mime="text/plain",
            use_container_width=True
        )