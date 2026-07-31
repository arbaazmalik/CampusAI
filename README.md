# 🎓 CampusAI

> An AI-powered academic assistant that enables students to chat with AI, interact with PDF documents, generate summaries, create MCQs, and prepare for viva examinations using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Groq](https://img.shields.io/badge/LLM-Groq_Llama_3.3-green)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success)
![FAISS](https://img.shields.io/badge/Vector_Database-FAISS-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 🚀 Live Demo

🔗 **Streamlit App:**  
https://campusai-nx24mexwmu84xjtznvx8gx.streamlit.app/

---

# 📖 Overview

CampusAI is an AI-powered academic assistant developed as a B.Tech Computer Science Engineering Major Project. It combines the power of Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and semantic search to provide an intelligent learning platform for students.

The application allows users to interact with AI, upload PDF notes, ask context-aware questions, generate concise summaries, create multiple-choice questions, and prepare for viva examinations—all through a clean and user-friendly interface.

Unlike traditional chatbots, CampusAI understands uploaded study materials using vector embeddings and semantic search, delivering accurate and context-aware responses.

---

# ✨ Features

## 🤖 AI Chat
- General-purpose AI assistant
- Powered by Groq Llama 3.3 70B
- Fast and intelligent responses
- Supports general academic queries

---

## 📄 Chat with PDF (RAG)
- Upload study material in PDF format
- Ask questions directly from the document
- Context-aware answers
- Uses Retrieval-Augmented Generation (RAG)
- FAISS vector database for semantic search

---

## 📝 PDF Summarizer
- Generate concise summaries
- Extract important concepts
- Helps students revise faster
- AI-generated structured summaries

---

## ❓ MCQ Generator
- Generate AI-powered multiple-choice questions
- Multiple answer options
- Correct answer included
- Useful for self-assessment and practice

---

## 🎤 Viva Question Generator
- Generate viva questions from uploaded PDFs
- Helps prepare for project viva
- AI-generated interview-style questions

---

# 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI & LLM
- Groq API
- Llama 3.3 70B

### RAG Pipeline
- LangChain
- FAISS
- Sentence Transformers

### PDF Processing
- PyPDF

### Other Libraries
- python-dotenv
- streamlit-option-menu

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
         Streamlit Web Interface
                  │
      ┌───────────┴───────────┐
      │                       │
      ▼                       ▼
 AI Chat Module         PDF Processing
                              │
                              ▼
                     Text Extraction
                              │
                              ▼
                     Text Chunking
                              │
                              ▼
                 Sentence Embeddings
                              │
                              ▼
                   FAISS Vector Store
                              │
                              ▼
                 Retrieval-Augmented Generation
                              │
                              ▼
                      Groq Llama 3.3
                              │
                              ▼
                        AI Response
```

---

# 📂 Project Structure

```
CampusAI/
│
├── app.py
│
├── chatbot/
│   ├── groq_client.py
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   ├── rag.py
│   ├── prompts.py
│   ├── summarizer.py
│   ├── mcq_generator.py
│   └── viva_generator.py
│
├── views/
│   ├── ai_chat.py
│   ├── pdf_chat.py
│   ├── summarizer.py
│   ├── mcq.py
│   └── viva.py
│
├── assets/
├── utils/
├── uploads/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/arbaazmalik/CampusAI.git
```

```bash
cd CampusAI
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Alternatively, for Streamlit Cloud deployment, add:

```
GROQ_API_KEY = YOUR_GROQ_API_KEY
```

inside **Streamlit Secrets**.

---

# ▶️ Run Locally

```bash
streamlit run app.py
```

---

# 📸 Application Modules

- 🤖 AI Chat
- 📄 Chat with PDF
- 📝 PDF Summarizer
- ❓ MCQ Generator
- 🎤 Viva Question Generator

---

# 🎯 Future Enhancements

- Voice-enabled AI Assistant
- OCR Support for Scanned PDFs
- Multi-language Support
- User Authentication
- Chat History
- PDF Export
- Cloud Database Integration
- Mobile App Version
- AI Flashcards
- Quiz Performance Analytics

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases (FAISS)
- Prompt Engineering
- LangChain
- Streamlit Application Development
- AI-powered Educational Systems

---

# 👨‍💻 Developer

**Arbaaz Malik**

B.Tech Computer Science & Engineering

GitHub: https://github.com/arbaazmalik

LinkedIn: https://www.linkedin.com/in/arbaaz-malik-2b55a92a3/

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

---

# 📜 License

This project is licensed under the MIT License.

Developed as a ** Generative AI Interan @IBM ** for educational and learning purposes.
