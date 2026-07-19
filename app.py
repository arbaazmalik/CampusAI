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

st.title("🎓 CampusAI")
st.caption("Your Intelligent Academic Assistant")

st.markdown(
    """
**Developed by**

**Arbaaz Malik**  
*Computer Science Engineer | AI Enthusiast*
"""
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
            "background-color": "#F3F1EC",
            "border-radius": "18px",
        },

        "icon": {
            "color": "#6B5B95",
            "font-size": "19px",
        },

        "nav-link": {
            "font-size": "16px",
            "padding": "12px",
            "margin": "6px",
            "border-radius": "12px",
            "color": "#2D2D2D",
            "--hover-color": "#ECE8F8",
        },

        "nav-link-selected": {
            "background-color": "#6B5B95",
            "color": "white",
            "font-weight": "600",
        },
    },
)
    st.markdown("---")

    st.caption("Powered by Groq")
    st.caption("Llama 3.3 70B")

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