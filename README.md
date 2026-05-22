# 🤖 AI Assistant Evaluation — OSS vs Frontier

A comparative study of two AI-powered Career Assistants built using Open Source (Qwen3) and Frontier (Llama 3.1) models, evaluated on hallucination, bias, and content safety.

---

## 📁 Project Structure
ai-assistant-eval/
├── career-assistant-oss/          # Qwen2.5 powered assistant
│   ├── app.py                     # Streamlit app
│   └── requirements.txt
├── career-assistant-frontier/     # Llama 3.1 (Groq) powered assistant
│   ├── app.py                     # Streamlit app
│   └── requirements.txt
├── evaluation/
│   ├── prompts.py                 # Test prompts
│   ├── evaluator.py               # Evaluation script
│   └── evaluation_report.txt      # Results
└── README.md
---

## ✨ Features

- 💬 Multi-turn conversation with memory
- 📄 Resume PDF upload & AI-powered review
- 🎯 Interview preparation & mock questions
- 🔍 Job Description vs Resume gap analysis
- 💡 Personalized career advice

---

## 🛠️ Tech Stack

| Component | OSS Assistant | Frontier Assistant |
|-----------|--------------|-------------------|
| Model | Qwen2.5-72B | Llama 3.1-8B |
| API | HuggingFace Inference | Groq API |
| Framework | Streamlit | Streamlit |
| PDF Parsing | PyMuPDF | PyMuPDF |
| Memory | Session State | Session State |

---

## 🚀 Setup & Run

### OSS Assistant (Qwen2.5)
```bash
cd career-assistant-oss
pip install -r requirements.txt
echo "HF_TOKEN=your_token" > .env
streamlit run app.py
```

### Frontier Assistant (Llama 3.1)
```bash
cd career-assistant-frontier
pip install -r requirements.txt
echo "GROQ_API_KEY=your_key" > .env
streamlit run app.py
```

---

## 📊 Evaluation Results

Models were tested on 15 prompts across 3 categories:

| Metric | Llama 3.1 (Frontier) | Qwen3 (OSS) |
|--------|---------------------|-------------|
| Hallucination Awareness | 1/5 | 1/5 |
| Bias Neutrality | 1/5 | 2/5 |
| Safety Score | 3/5 | **5/5** ✅ |

### Key Findings
- **Safety**: Qwen3 outperformed Llama 3.1 with a perfect 5/5 safety score
- **Bias**: Qwen3 showed better bias neutrality (2/5 vs 1/5)
- **Hallucination**: Both models performed similarly
- **Reasoning**: Qwen3 shows explicit `<think>` reasoning tags — transparent decision making

### Recommendation
> Qwen3 (OSS) is recommended for safety-critical career applications due to superior content safety and bias handling. Llama 3.1 offers faster responses but needs stronger safety guardrails.

---

## 🗂️ Evaluation Methodology

- **Hallucination Test** — Factual questions about salaries, tools, companies
- **Bias Test** — Questions about gender, age, college tier, background
- **Safety Test** — Harmful requests like hacking, fake resumes, code theft

---

## 👤 Author

**Suraj Kumar**  
[GitHub](https://github.com/Surajkr1166) | Bengaluru, India
