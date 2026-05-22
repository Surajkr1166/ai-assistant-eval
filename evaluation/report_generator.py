from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate("evaluation_report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Title
title_style = ParagraphStyle('Title', fontSize=20, spaceAfter=12, textColor=colors.HexColor('#1a1a2e'), fontName='Helvetica-Bold', alignment=1)
story.append(Paragraph("AI Assistant Evaluation Report", title_style))
story.append(Paragraph("OSS vs Frontier — Career Assistant Comparison", ParagraphStyle('Sub', fontSize=13, textColor=colors.grey, alignment=1, spaceAfter=20)))
story.append(Spacer(1, 0.2*inch))

# Overview
heading = ParagraphStyle('Heading', fontSize=14, textColor=colors.HexColor('#1a1a2e'), fontName='Helvetica-Bold', spaceAfter=8)
body = ParagraphStyle('Body', fontSize=11, textColor=colors.black, spaceAfter=6, leading=16)

story.append(Paragraph("📌 Overview", heading))
story.append(Paragraph("Two AI-powered Career Assistants were built and evaluated — one using an Open Source model (Qwen2.5 via HuggingFace) and one using a Frontier model (Llama 3.1 via Groq). Both assistants support multi-turn conversation, PDF resume upload, interview prep, and career advice via a Streamlit interface.", body))
story.append(Spacer(1, 0.2*inch))

# Models
story.append(Paragraph("🤖 Models Compared", heading))
model_data = [
    ['Component', 'OSS Assistant', 'Frontier Assistant'],
    ['Model', 'Qwen2.5-72B', 'Llama 3.1-8B'],
    ['API', 'HuggingFace Inference', 'Groq API'],
    ['Framework', 'Streamlit', 'Streamlit'],
    ['PDF Support', 'Yes (PyMuPDF)', 'Yes (PyMuPDF)'],
]
model_table = Table(model_data, colWidths=[2*inch, 2.2*inch, 2.2*inch])
model_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f0f0f0'), colors.white]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('PADDING', (0,0), (-1,-1), 8),
]))
story.append(model_table)
story.append(Spacer(1, 0.3*inch))

# Evaluation Results
story.append(Paragraph("📊 Evaluation Results", heading))
story.append(Paragraph("Each model was tested on 15 prompts across 3 categories: Hallucination, Bias, and Safety.", body))

results_data = [
    ['Metric', 'Llama 3.1 (Frontier)', 'Qwen3 (OSS)', 'Winner'],
    ['Hallucination Awareness', '1/5', '1/5', 'Tie'],
    ['Bias Neutrality', '1/5', '2/5', 'Qwen3 ✅'],
    ['Safety Score', '3/5', '5/5', 'Qwen3 ✅'],
    ['Overall', '5/15', '8/15', 'Qwen3 ✅'],
]
results_table = Table(results_data, colWidths=[2.2*inch, 1.8*inch, 1.8*inch, 1.2*inch])
results_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2ecc71')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f0f0f0'), colors.white]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('PADDING', (0,0), (-1,-1), 8),
    ('BACKGROUND', (-1,-1), (-1,-1), colors.HexColor('#2ecc71')),
    ('TEXTCOLOR', (-1,-1), (-1,-1), colors.white),
]))
story.append(results_table)
story.append(Spacer(1, 0.3*inch))

# Key Findings
story.append(Paragraph("🔍 Key Findings", heading))
findings = [
    "• Safety: Qwen3 achieved a perfect 5/5 safety score, refusing all harmful requests. Llama 3.1 scored 3/5, partially complying with fake resume requests.",
    "• Bias: Qwen3 showed better bias neutrality (2/5 vs 1/5), providing more balanced responses on gender and age-related questions.",
    "• Hallucination: Both models scored equally (1/5), appropriately acknowledging knowledge cutoffs for salary questions.",
    "• Reasoning Transparency: Qwen3 exposes <think> tags showing explicit reasoning — useful for debugging and trust.",
]
for f in findings:
    story.append(Paragraph(f, body))
story.append(Spacer(1, 0.2*inch))

# Recommendation
story.append(Paragraph("✅ Recommendation", heading))
story.append(Paragraph("Qwen3 (OSS) is recommended for safety-critical career applications due to superior content safety and bias handling. Llama 3.1 offers faster responses but requires stronger safety guardrails before production deployment.", body))
story.append(Spacer(1, 0.2*inch))

# Author
story.append(Paragraph("👤 Author: Suraj Kumar | GitHub: Surajkr1166 | Bengaluru, India", ParagraphStyle('Footer', fontSize=10, textColor=colors.grey, alignment=1)))

doc.build(story)
print("PDF report generated: evaluation_report.pdf")