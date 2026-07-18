# 🎓 CampusAI

> An AI-powered academic assistant built using Python, Streamlit, Groq Llama 3.3, RAG, and FAISS to help students learn smarter.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Groq](https://img.shields.io/badge/LLM-Groq_Llama_3.3-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Overview

CampusAI is an AI-powered academic assistant designed to simplify the learning experience for students. It enables users to chat with AI, interact with PDF documents, generate summaries, create multiple-choice questions, and prepare for viva examinations—all from a single intuitive interface.

The project leverages Retrieval-Augmented Generation (RAG) to provide context-aware answers from uploaded PDF documents, making it a practical AI solution for education.

---

## ✨ Features

### 🤖 AI Chat
- General-purpose AI assistant
- Powered by Groq Llama 3.3 70B
- Fast and accurate responses

### 📄 Chat with PDF
- Upload PDF documents
- Ask questions based on document content
- Uses RAG with FAISS vector database

### 📝 PDF Summarizer
- Generate concise summaries
- Extract key concepts
- Save study time

### ❓ MCQ Generator
- Automatically generate multiple-choice questions
- AI-generated answer options
- Useful for self-assessment

### 🎤 Viva Question Generator
- Generate viva questions from study material
- Helps students prepare for interviews and examinations

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Groq API (Llama 3.3 70B)
- LangChain
- FAISS
- Sentence Transformers
- PyPDF
- RAG (Retrieval-Augmented Generation)

---

# 📂 Project Structure

```
CampusAI/
│
├── app.py
├── chatbot/
│   ├── groq_client.py
│   ├── pdf_loader.py
│   ├── rag.py
│   ├── vector_store.py
│   ├── text_splitter.py
│   ├── mcq_generator.py
│   ├── summarizer.py
│   └── viva_generator.py
│
├── views/
│   ├── ai_chat.py
│   ├── pdf_chat.py
│   ├── summarizer.py
│   ├── mcq.py
│   └── viva.py
│
├── utils/
├── assets/
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/arbaazmalik/CampusAI.git
```

```
cd CampusAI
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# ▶️ Run the Project

```bash
streamlit run app.py
```

--


# 🎯 Future Enhancements

- Voice Assistant
- OCR Support
- Multi-language Support
- Chat History
- User Authentication
- Cloud Deployment
- Mobile Responsive UI

---

# 👨‍💻 Developer

**Arbaaz Malik**

B.Tech Computer Science Engineering

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is developed for educational purposes as a B.Tech Major Project.
