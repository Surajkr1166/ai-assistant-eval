# 🤖 AI Assistant Evaluation — OSS vs Frontier

Comparing two AI-powered Career Assistants built with Open Source (Qwen2.5) and Frontier (Llama 3.1 via Groq) models.

## 📁 Project Structure
ai-assistant-eval/
├── career-assistant-oss/      # Qwen2.5 powered assistant
│   ├── app.py
│   └── requirements.txt
├── career-assistant-frontier/ # Llama 3.1 (Groq) powered assistant
│   ├── app.py
│   └── requirements.txt
└── README.md
## ✨ Features

- 💬 Multi-turn conversation with memory
- 📄 Resume PDF upload & review
- 🎯 Interview preparation
- 🔍 Job Description vs Resume gap analysis
- 💡 Career advice

## 🛠️ Tech Stack

| Component | OSS Assistant | Frontier Assistant |
|-----------|--------------|-------------------|
| Model | Qwen2.5-72B | Llama 3.1-8B (Groq) |
| Framework | Streamlit | Streamlit |
| PDF Parsing | PyMuPDF | PyMuPDF |
| API | HuggingFace Inference | Groq API |

## 🚀 Setup & Run

### OSS Assistant
```bash
cd career-assistant-oss
pip install -r requirements.txt
# Add HF_TOKEN in .env file
streamlit run app.py
```

### Frontier Assistant
```bash
cd career-assistant-frontier
pip install -r requirements.txt
# Add GROQ_API_KEY in .env file
streamlit run app.py
```

## 📊 Evaluation

Models evaluated on:
- **Hallucination Rate** — factual accuracy
- **Bias & Harmful Outputs** — stereotype detection
- **Content Safety** — jailbreak resistance

## 👤 Author
Suraj — [GitHub](https://github.com/Surajkr1166)
