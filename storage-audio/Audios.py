import pyttsx3
import os

engine = pyttsx3.init()

output_dir = r"E:\Zecpath_AI_pro\Data\raw\Audios"
os.makedirs(output_dir, exist_ok=True)

scripts = [
    "I have handled GST return filing including GSTR-1 and GSTR-3B. I ensured timely compliance and reconciled input tax credit regularly.",
    "I worked on direct and indirect taxation including income tax return filing and tax planning for clients.",
    "I assisted in statutory audits and internal audits, ensuring compliance with accounting standards and identifying financial discrepancies.",
    "I prepared balance sheets and profit and loss statements.",
    "I managed TDS calculations, deductions, and return filings while ensuring compliance with government regulations.",
    "I performed financial analysis to evaluate business performance and provided insights for cost optimization.",
    "I handled corporate accounting activities.",
    "I maintained bookkeeping using Tally.",
    "I ensured statutory compliance and ROC filings.",
    "I worked on budgeting and forecasting.",
    "I interacted with clients to understand their financial needs and provided solutions for taxation and compliance.",
    "I participated in GST audits.",
    "I prepared MIS reports.",
    "I performed bank reconciliation.",
    "I worked on cost accounting techniques."
]

for i, text in enumerate(scripts, 1):
    file_path = os.path.join(output_dir, f"audio_{i}.wav")
    engine.save_to_file(text, file_path)

engine.runAndWait()

print("✅ All audio files generated!")