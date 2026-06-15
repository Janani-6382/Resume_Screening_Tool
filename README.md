# Resume_Screening_Tool
AI-powered resume screening tool that analyzes resumes, matches them with job descriptions, ranks candidates based on relevance, and generates detailed reports using Python, Flask, and NLP techniques.
# AI Resume Screening Tool

## 📌 Project Overview
The AI Resume Screening Tool is a web-based application that helps recruiters and hiring teams automatically analyze resumes and match them with job descriptions. The system extracts text from uploaded resumes, calculates matching scores, and ranks candidates based on their suitability for a specific role.

## 🚀 Features
- Resume Upload (PDF/DOCX)
- Resume Text Extraction
- Job Description Matching
- Resume Scoring System
- Candidate Ranking
- User-Friendly Web Interface
- PDF Report Generation
- Fast and Accurate Screening

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- Bootstrap

### Backend
- Python
- Flask

### Libraries
- PyPDF2
- python-docx
- pandas
- scikit-learn
- nltk
- reportlab

## 📂 Project Structure

AI_Resume_Screening_Tool/
│
├── app.py
├── requirements.txt
├── README.md
│
├── uploads/
│ └── resumes
│
├── templates/
│ ├── index.html
│ └── results.html
│
├── static/
│ ├── css
│ └── images
│
├── reports/
│ └── generated_reports
│
└── resume_parser.py

## Installation

1. Download or clone the repository.
2. Open the project folder in VS Code.
3. Install required packages:

pip install -r requirements.txt

4. Run the application:

python app.py

5. Open:

https://resume-screening-tool-59uo.onrender.com
