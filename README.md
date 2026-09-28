# 🧭 AI Learning Roadmap Generator

An AI-powered learning roadmap generator built with Python, Streamlit, and Groq.

## Features

- Personalized learning roadmaps
- Beginner, Intermediate, and Advanced levels
- Custom learning duration
- Hours-per-week planning
- Personalized learning goals
- Weekly topics and practice tasks
- Mini projects and final project recommendations

## Tech Stack

- Python
- Streamlit
- Groq API
- OpenAI GPT-OSS 120B through Groq

## How It Works

User Input → Prompt Generation → Groq API → AI-generated Learning Roadmap

## Deployment

This project is designed to be deployed using Streamlit Community Cloud.

Add your Groq API key in Streamlit Cloud Secrets:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Do not upload your API key to GitHub.

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Then configure your Streamlit secret and run:

```bash
streamlit run app.py
```
