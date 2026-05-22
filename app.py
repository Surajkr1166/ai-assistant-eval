import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF

load_dotenv(override=True)
token = os.getenv("HF_TOKEN")

client = InferenceClient(
    model="Qwen/Qwen2.5-72B-Instruct",
    token=token
)

SYSTEM_PROMPT = """You are an expert Career & Resume Assistant. You help users with:
1. Resume review and improvement suggestions
2. Interview preparation and mock questions
3. Job description vs resume gap analysis
4. Career advice and job search strategies

Be specific, actionable, and encouraging. Ask clarifying questions when needed."""

st.set_page_config(page_title="Career Assistant (OSS)", page_icon="💼")
st.title("💼 Career Assistant — Powered by Qwen2.5")
st.caption("Your AI-powered career coach for resume, interviews & job search")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

with st.sidebar:
    st.header("🛠️ Features")
    st.markdown("""
    - 📄 **Resume Review**
    - 🎯 **Interview Prep**
    - 🔍 **JD Match Analysis**
    - 💡 **Career Advice**
    """)

    st.divider()
    st.subheader("📎 Upload Resume (PDF)")
    uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

    if uploaded_file is not None:
        pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in pdf_doc:
            text += page.get_text()
        st.session_state.resume_text = text
        st.success("✅ Resume uploaded!")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me anything about your career..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    system = SYSTEM_PROMPT
    if st.session_state.resume_text:
        system += f"\n\nUser's Resume:\n{st.session_state.resume_text}"

    api_messages = [{"role": "system", "content": system}]
    api_messages += st.session_state.messages

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat_completion(
                messages=api_messages,
                max_tokens=1024,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})