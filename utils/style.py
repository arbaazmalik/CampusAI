import streamlit as st


def load_css():
    st.markdown("""
<style>

/* ===========================
   Google Font
=========================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}

/* ===========================
   Main App
=========================== */

.stApp{
    background:#FFF8F0;
}

/* ===========================
   Sidebar
=========================== */

section[data-testid="stSidebar"]{
    background:#EFE6D8;
    border-right:1px solid #D8CDBD;
}

section[data-testid="stSidebar"] *{
    color:#2F3437;
}

/* ===========================
   Headings
=========================== */

h1{
    color:#202123;
    font-weight:700;
}

h2,h3,h4{
    color:#2F2F2F;
    font-weight:600;
}

/* ===========================
   Main Container
=========================== */

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1200px;
}

/* ===========================
   Buttons
=========================== */

.stButton>button{

    width:100%;

    border:none;

    border-radius:14px;

    background:#6B5B95;

    color:white;

    padding:12px;

    font-size:15px;

    font-weight:600;

    transition:0.3s;
}

.stButton>button:hover{

    background:#5A4B84;

    transform:translateY(-2px);

    box-shadow:0 6px 20px rgba(0,0,0,.18);

}

/* ===========================
   Inputs
=========================== */

.stTextInput input,
.stTextArea textarea{

    background:#EFE6D8 !important;

    border:1px solid #D8CDBD !important;

    border-radius:16px;

    color:#2F3437 !important;

    padding:12px;

}
                
/* ===========================
   File Uploader
=========================== */

[data-testid="stFileUploader"]{
    border:2px dashed #D8CDBD;
    border-radius:18px;
    padding:18px;
    background:#F8F3EA;
}
/* ===========================
   Radio
=========================== */

.stRadio{

    background:#F8F3EA;

    padding:15px;

    border-radius:14px;

}

/* ===========================
   Success
=========================== */

.stSuccess{

    border-radius:14px;

}

/* ===========================
   Error
=========================== */

.stError{

    border-radius:14px;

}

/* ===========================
   Info
=========================== */

.stInfo{

    border-radius:14px;

}

/* ===========================
   Progress
=========================== */

.stProgress > div > div{

    border-radius:20px;

}

/* ===========================
   Download Button
=========================== */

.stDownloadButton>button{

    width:100%;

    border-radius:14px;

}

/* ===========================
   Divider
=========================== */

hr{

    margin-top:30px;

    margin-bottom:30px;

}

/* ===========================
   Chat Input
=========================== */

[data-testid="stChatInput"]{
    background:#EFE6D8 !important;
    border:1px solid #D8CDBD !important;
    border-radius:18px !important;
}

[data-testid="stChatInput"] > div{
    background:#EFE6D8 !important;
    border-radius:18px !important;
}

[data-testid="stChatInput"] textarea{
    background:#EFE6D8 !important;
    color:#2F3437 !important;
}

[data-testid="stChatInput"] textarea::placeholder{
    color:#7A746C !important;
}

[data-testid="stChatInput"] button{
    background:#6B5B95 !important;
    color:white !important;
    border-radius:12px !important;
}

[data-testid="stChatInput"] button:hover{
    background:#5A4B84 !important;
}

</style>
""", unsafe_allow_html=True)
    
