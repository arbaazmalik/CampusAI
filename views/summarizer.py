import streamlit as st

from chatbot.summarizer import summarize_pdf


def show():

    st.title("📚 PDF Summarizer")
    st.caption("Convert lengthy PDFs into concise study notes with AI.")

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        key="summary_pdf"
    )

    if uploaded_pdf is None:

        st.info("📄 Upload a PDF to generate an AI-powered summary.")
        return

    pdf_path = f"uploads/{uploaded_pdf.name}"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())

    if st.button("📝 Generate Summary", use_container_width=True):

        with st.spinner("Generating summary..."):

            summary = summarize_pdf(pdf_path)

        st.divider()

        st.subheader("📖 Summary")

        st.markdown(summary)

        st.download_button(
            "📥 Download Summary",
            summary,
            file_name="summary.txt",
            mime="text/plain",
            use_container_width=True
        )