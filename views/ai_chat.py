import streamlit as st

from chatbot.groq_client import stream_response


def show():

    st.title("🤖 AI Chat")
    st.caption("Ask questions, solve doubts, and learn faster with CampusAI.")

    st.markdown('<div class="page-card">', unsafe_allow_html=True)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display previous conversation
    for message in st.session_state["messages"]:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input("Ask anything...")

    if prompt:

        # Save user message
        st.session_state["messages"].append(
            {
                "role": "user",
                "content": prompt
            }
        )

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate AI response with conversation history
        with st.chat_message("assistant"):

            response = st.write_stream(
                stream_response(
                    st.session_state["messages"]
                )
            )

        # Save AI response
        st.session_state["messages"].append(
            {
                "role": "assistant",
                "content": response
            }
        )

    st.markdown("</div>", unsafe_allow_html=True)