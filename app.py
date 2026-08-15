from views.mcq import show as mcq
from views.viva import show as viva
from streamlit_option_menu import option_menu
from views.summarizer import show as summarizer
import streamlit as st

from utils.style import load_css

from views.ai_chat import show as ai_chat
from views.pdf_chat import show as pdf_chat


st.set_page_config(
    page_title="CampusAI",
    page_icon="🎓",
    layout="wide",
)

load_css()
st.markdown(
    """
    <div class="mobile-sidebar-hint">
        Tap for more options
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
"""
<div class="campus-header">
<div class="campus-title">
<h1>🎓 CampusAI</h1>
<p>Your Intelligent Academic Assistant</p>
</div>
<div class="campus-developer">
<span>Developed by Arbaaz Malik | AI Enthusiast</span>
</div>
</div>
""",
unsafe_allow_html=True
)

with st.sidebar:

    st.markdown(
        """
        # 🎓 CampusAI
        ### AI Academic Assistant
        ---
        """
    )

    feature = option_menu(
        menu_title=None,
        options=[
            "AI Chat",
            "Chat with PDF",
            "MCQ Generator",
            "PDF Summarizer",
            "Viva Generator",
        ],
        icons=[
            "chat-dots",
            "file-earmark-pdf",
            "patch-question",
            "journal-text",
            "mic",
        ],
        default_index=0,
        styles={
            "container": {
                "padding": "8px",
                "background-color": "#F7F3EA",
                "border-radius": "18px",
            },

            "icon": {
                "color": "#2563EB",
                "font-size": "19px",
            },

            "nav-link": {
                "font-size": "16px",
                "padding": "12px",
                "margin": "6px",
                "border-radius": "12px",
                "color": "#1F2937",
                "--hover-color": "#E8F0FF",
            },

            "nav-link-selected": {
                "background-color": "#2563EB",
                "color": "white",
                "font-weight": "600",
            },
        },
    )

    # New Chat button
    if st.button(
        "🗑️  New Chat",
        use_container_width=True,
        key="new_chat_sidebar",
    ):
        st.session_state["messages"] = []
        st.rerun()

    st.markdown("---")

    st.caption("Powered by Groq")
    st.caption("Llama 3.3 70B")


# -----------------------------
# Feature Routing
# -----------------------------

if feature == "AI Chat":
    ai_chat()

elif feature == "Chat with PDF":
    pdf_chat()

elif feature == "MCQ Generator":
    mcq()

elif feature == "PDF Summarizer":
    summarizer()

elif feature == "Viva Generator":
    viva()