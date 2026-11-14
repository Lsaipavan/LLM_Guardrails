# LLM Guardrails

An AI-powered application built using **FastAPI and Google Gemini** to demonstrate input and output guardrails for Large Language Model (LLM) applications.

## 🚀 Project Overview

Large Language Models can sometimes generate inaccurate, unsafe, or inappropriate responses. LLM Guardrails help validate user inputs and AI-generated outputs to improve the reliability and safety of AI applications.

This project demonstrates how guardrails can be integrated into a Gemini-powered application using FastAPI.

## ✨ Features

- Google Gemini API integration
- Input validation using guardrails
- Output response validation
- FastAPI backend
- Web interface using HTML, CSS, and JavaScript
- Environment-based configuration for API credentials

## 🛠️ Technologies Used

- Python
- FastAPI
- Google Gemini API
- Pydantic
- HTML
- CSS
- JavaScript

## 📂 Project Structure

```text
LLM_Guardrails/
│
├── app.py
├── config.py
├── gemini_service.py
├── guardrails.py
├── output_guardrails.py
├── requirements.txt
├── .env
├── .gitignore
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    └── index.html
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Lsaipavan/LLM_Guardrails.git
```

### 2. Navigate to the project directory

```bash
cd LLM_Guardrails
```

### 3. Create a virtual environment

```bash
python -m venv myenv
```

### 4. Activate the environment (Windows)

```bash
myenv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API credentials

Create a `.env` file and add your Gemini API key using the variable expected by `config.py`.

**Never upload your API key to GitHub.**

### 7. Run the application

```bash
uvicorn app:app --reload
```

### 8. Open in browser

```text
http://127.0.0.1:8000
```

## 🎯 Learning Outcomes

- Understanding LLM Guardrails
- Integrating Google Gemini API
- Building APIs with FastAPI
- Validating AI inputs and outputs
- Managing environment variables
- Structuring and managing Python projects

## 👨‍💻 Author

**Saipavan Lingampelli**

GitHub: [Lsaipavan](https://github.com/Lsaipavan)

---

⭐ If you find this project useful, feel free to explore and learn from it.
