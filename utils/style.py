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
   Color Palette
=========================== */

/*
   Beach Background: #F7F3EA
   Card White:        #FFFDF8
   Sidebar Beach:    #F1E9DA

   Primary Blue:     #2563EB
   Dark Blue:        #1D4ED8
   Light Blue:       #E8F0FF

   Text:             #1F2937
   Secondary Text:   #64748B
   Border:           #E5DED2
*/


/* ===========================
   Main App
=========================== */

.stApp{
    background:#F7F3EA;
}


/* ===========================
   Sidebar
=========================== */

section[data-testid="stSidebar"]{
    background:#F1E9DA;
    border-right:1px solid #E5DED2;
}

section[data-testid="stSidebar"] *{
    color:#1F2937;
}


/* ===========================
   Headings
=========================== */

h1{
    color:#1F2937;
    font-weight:700;
}

h2,h3,h4{
    color:#1F2937;
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
   CampusAI Header
=========================== */

.campus-header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:35px;
}

.campus-title h1{
    margin:0;
    color:#1F2937;
    font-size:42px;
    font-weight:700;
}

.campus-title p{
    margin:6px 0 0 0;
    color:#64748B;
    font-size:16px;
}

.campus-developer{
    text-align:right;
    display:flex;
    flex-direction:column;
    gap:3px;
}

.campus-developer span{
    color:#64748B;
    font-size:13px;
}

.campus-developer strong{
    color:#1F2937;
    font-size:15px;
}

.campus-developer em{
    color:#64748B;
    font-size:13px;
}

/* ===========================
   Buttons
=========================== */

.stButton>button{

    width:100%;

    border:1px solid #2563EB;

    border-radius:14px;

    background:#2563EB;

    color:white;

    padding:12px;

    font-size:15px;

    font-weight:600;

    transition:0.3s;
}

/* ===========================
   Sidebar New Chat Button
=========================== */

section[data-testid="stSidebar"] .stButton>button{
    background:#FFFDF8 !important;
    color:#1F2937 !important;
    border:1px solid #E5DED2 !important;
    box-shadow:none !important;
    transform:none !important;
}

section[data-testid="stSidebar"] .stButton>button:hover{
    background:#F1E9DA !important;
    color:#1F2937 !important;
    border-color:#D8CDBD !important;
    box-shadow:none !important;
    transform:none !important;
}

.stButton>button:hover{

    background:#1D4ED8;

    border-color:#1D4ED8;

    transform:translateY(-2px);

    box-shadow:0 6px 20px rgba(37,99,235,0.20);

}

/* ===========================
   Inputs
=========================== */

.stTextInput input,
.stTextArea textarea{

    background:#FFFDF8 !important;

    border:1px solid #E5DED2 !important;

    border-radius:16px;

    color:#1F2937 !important;

    padding:12px;

}

.stTextInput input:focus,
.stTextArea textarea:focus{

    border-color:#2563EB !important;

    box-shadow:0 0 0 1px #2563EB !important;

}


/* ===========================
   File Uploader
=========================== */

[data-testid="stFileUploader"]{

    border:2px dashed #B8C8E8;

    border-radius:18px;

    padding:18px;

    background:#FFFDF8;
}

[data-testid="stFileUploader"]:hover{

    border-color:#2563EB;

    background:#F8FAFF;
}


/* ===========================
   Radio
=========================== */

.stRadio{

    background:#FFFDF8;

    padding:15px;

    border-radius:14px;

    border:1px solid #E5DED2;

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

    background:#2563EB;

    color:white;

    border:1px solid #2563EB;

}

.stDownloadButton>button:hover{

    background:#1D4ED8;

    border-color:#1D4ED8;

}


/* ===========================
   Divider
=========================== */

hr{

    margin-top:30px;

    margin-bottom:30px;

    border-color:#E5DED2;

}


/* ===========================
   Chat Input
=========================== */

[data-testid="stChatInput"]{

    background:#FFFDF8 !important;

    border:1px solid #E5DED2 !important;

    border-radius:18px !important;

}

[data-testid="stChatInput"] > div{

    background:#FFFDF8 !important;

    border-radius:18px !important;

}

[data-testid="stChatInput"] textarea{

    background:#FFFDF8 !important;

    color:#1F2937 !important;

}

[data-testid="stChatInput"] textarea::placeholder{

    color:#64748B !important;

}


/* ===========================
   Chat Send Button
=========================== */

[data-testid="stChatInput"] button{

    background:#2563EB !important;

    color:white !important;

    border-radius:12px !important;

}

[data-testid="stChatInput"] button:hover{

    background:#1D4ED8 !important;

}


/* ===========================
   Chat Messages
=========================== */

/* User message */

[data-testid="stChatMessage"]{

    border-radius:16px;

}


/* ===========================
   Links
=========================== */

a{

    color:#2563EB !important;

}

a:hover{

    color:#1D4ED8 !important;

}


/* ===========================
   Selectbox
=========================== */

[data-baseweb="select"] > div{

    background:#FFFDF8 !important;

    border-color:#E5DED2 !important;

    border-radius:14px !important;

}


/* ===========================
   Slider
=========================== */

[data-testid="stSlider"] [role="slider"]{

    background:#2563EB;

}


/* ===========================
   Checkbox
=========================== */

[data-testid="stCheckbox"]{

    accent-color:#2563EB;

}


/* ===========================
   Mobile
=========================== */

@media (max-width:768px){

    .block-container{

        padding-top:1.2rem;

        padding-left:1rem;

        padding-right:1rem;

    }

    h1{

        font-size:1.8rem;

    }

    h2{

        font-size:1.4rem;

    }

    .stButton>button{

        border-radius:12px;

    }

}


/* ===========================
   Prevent Dark Mode Changes
=========================== */

@media (prefers-color-scheme: dark){

    .stApp{

        background:#F7F3EA !important;

    }

    section[data-testid="stSidebar"]{

        background:#F1E9DA !important;

    }

    h1,h2,h3,h4,p,span,label{

        color:#1F2937;

    }

}

</style>
""", unsafe_allow_html=True)