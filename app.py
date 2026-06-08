from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from docx import Document

app = Flask(__name__)

SKILLS_DB = [
    "python", "java", "sql", "flask", "html", "css",
    "javascript", "react", "machine learning", "excel",
    "recruitment", "payroll", "communication",
    "employee relations", "git", "rest api"
]

def extract_pdf_text(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + " "

    return text.lower()

def extract_docx_text(file):
    doc = Document(file)
    text = ""

    for para in doc.paragraphs:
        text += para.text + " "

    return text.lower()

def extract_txt_text(file):
    return file.read().decode("utf-8").lower()

def extract_skills(text):
    return [skill for skill in SKILLS_DB if skill in text]

@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        jd_text = request.form.get("jd_text", "")
        jd_file = request.files.get("jd_file")
        resume_file = request.files.get("resume_file")

        job_description = ""

        if jd_text.strip():
            job_description = jd_text.lower()

        elif jd_file and jd_file.filename:

            if jd_file.filename.endswith(".pdf"):
                job_description = extract_pdf_text(jd_file)

            elif jd_file.filename.endswith(".docx"):
                job_description = extract_docx_text(jd_file)

            elif jd_file.filename.endswith(".txt"):
                job_description = extract_txt_text(jd_file)

        if resume_file and resume_file.filename:

            if resume_file.filename.endswith(".pdf"):
                resume_text = extract_pdf_text(resume_file)

            elif resume_file.filename.endswith(".docx"):
                resume_text = extract_docx_text(resume_file)

            else:
                return "Resume must be PDF or DOCX"

            jd_skills = extract_skills(job_description)
            resume_skills = extract_skills(resume_text)

            matched = list(set(jd_skills) & set(resume_skills))
            missing = list(set(jd_skills) - set(resume_skills))

            score = round(
                (len(matched) / len(jd_skills)) * 100,
                2
            ) if jd_skills else 0

            result = {
                "filename": resume_file.filename,
                "score": score,
                "matched": matched,
                "missing": missing
            }

            print(result)

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
