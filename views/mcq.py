import os

import streamlit as st

from chatbot.mcq_generator import generate_mcq_from_pdf


def show():

    st.header("📝 MCQ Generator")

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        key="mcq_pdf"
    )

    num_questions = st.slider(
        "Number of Questions",
        5,
        30,
        10
    )

    if uploaded_pdf is not None:

     os.makedirs("uploads", exist_ok=True)

    pdf_path = f"uploads/{uploaded_pdf.name}"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())

        col1, col2 = st.columns(2)

        with col1:

            if st.button("Generate Quiz"):

                with st.spinner("Generating Questions..."):

                    st.session_state["mcqs"] = generate_mcq_from_pdf(
                        pdf_path,
                        num_questions
                    )


                st.session_state["submitted"] = False

        with col2:

            if st.button("New Quiz"):

                st.session_state.pop("mcqs", None)
                st.session_state.pop("submitted", None)

                st.rerun()

    if "mcqs" not in st.session_state:
        return

    score = 0

    total = len(st.session_state["mcqs"])

    st.write(f"Total Questions : {total}")

    for i, mcq in enumerate(st.session_state["mcqs"]):

        st.markdown(f"## Question {i+1}")

        st.write(mcq["question"])

        st.radio(
            "Choose one",
            mcq["options"],
            key=f"mcq_{i}"
        )

    if st.button("Submit Quiz"):

        st.session_state["submitted"] = True

    if st.session_state.get("submitted", False):

        st.divider()

        for i, mcq in enumerate(st.session_state["mcqs"]):

            selected = st.session_state[f"mcq_{i}"]

            correct_option = mcq["options"][mcq["answer"]]

            if selected == correct_option:
                score += 1

            st.markdown(f"### Question {i+1}")

            st.write(mcq["question"])

            st.write(f"**Your Answer:** {selected}")

            st.write(f" **Correct Answer:** {correct_option}")

            if selected == correct_option:
                st.success("✅ Correct")
            else:
                st.error("❌ Incorrect")

        st.divider()

        st.success(f"Final Score : {score}/{total}")

        st.info(f"Percentage : {(score/total)*100:.2f}%")