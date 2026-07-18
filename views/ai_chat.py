import streamlit as st

from chatbot.groq_client import generate_response


def show():

    st.title("🤖 AI Chat")
    st.caption("Ask questions, solve doubts, and learn faster with CampusAI.")

    st.markdown('<div class="page-card">', unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask anything...")

    if prompt:

        st.session_state["messages"].append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):
                response = generate_response(prompt)

            st.markdown(response)

        st.session_state["messages"].append(
            {
                "role": "assistant",
                "content": response
            }
        )

    st.markdown("</div>", unsafe_allow_html=True)