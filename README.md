# 🤖 LLM ChatBot

## 📌 Overview
LLM ChatBot is an AI-powered chatbot application designed to provide intelligent conversations and various functionalities such as file-based Q&A, web-enhanced search, Langchain utilities, and user feedback integration. Users must enter their OpenAI API key to access the app.

---

## ✨ Features

1. **💬 ChatBot** - Standard chatbot functionality allowing users to interact with an LLM-powered assistant.
2. **📂 File Q&A** - Users can upload a document (PDF, TXT, DOCX) and ask questions based on its content.
3. **🔍 Chat with Search** - Enhances responses by fetching relevant information from online sources before answering.
4. **⚡ Langchain Quick Start** - Provides a simple Langchain implementation for chaining LLM responses effectively.
5. **📝 Langchain Prompt Template** - Allows users to create structured prompts using Langchain's templating system.
6. **⭐ Chat with User Feedback** - Users can rate responses and provide feedback for improving future interactions.

---

## 📋 Prerequisites
- 🐍 Python 3.8+
- 🔑 OpenAI API Key

---

## 🚀 Installation Guide

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/llm-chatbot.git
cd llm-chatbot
```

### 🔹 Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### 🔹 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Step 4: Set OpenAI API Key
Create a `.env` file and add your OpenAI API key:
```plaintext
OPENAI_API_KEY=your_api_key_here
```
Alternatively, set it as an environment variable:
```bash
export OPENAI_API_KEY=your_api_key_here  # macOS/Linux
set OPENAI_API_KEY=your_api_key_here  # Windows
```

---

## ▶️ Usage

### 🎯 Run the Application
```bash
python app.py
```

### 🌐 Available Endpoints
| Endpoint | Description |
|----------|-------------|
| `/chat` | 💬 Standard chatbot interaction |
| `/file-qa` | 📂 File-based Q&A processing |
| `/search-chat` | 🔍 Enhanced chat with search capabilities |
| `/langchain-quickstart` | ⚡ Simple Langchain response chaining |
| `/langchain-prompt` | 📝 Prompt templating with Langchain |
| `/feedback` | ⭐ User feedback submission |

---

## 🤝 Contributing
We welcome contributions! Feel free to submit issues and pull requests to improve this chatbot. 

---

## 📜 License
This project is licensed under the MIT License.
