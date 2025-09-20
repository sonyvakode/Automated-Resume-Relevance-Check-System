# Automated Resume Relevance Check System

## Overview
At Innomatics Research Labs, the process of evaluating resumes is currently manual, inconsistent, and time-consuming. Each week, placement teams across Hyderabad, Bangalore, Pune, and Delhi NCR receive 18–20 job requirements, with each posting attracting thousands of applications.  

This system automates resume evaluation to:
- Generate a **Relevance Score** (0–100) for each resume per job role.
- Highlight **missing skills, certifications, or projects**.
- Provide a **fit verdict** (High / Medium / Low suitability) for recruiters.
- Offer **personalized improvement feedback** to students.
- Store evaluations in a **web-based dashboard** accessible to the placement team.

---

## Problem Statement
Manual resume evaluation causes:
- Delays in shortlisting candidates.
- Inconsistent judgments due to evaluator subjectivity.
- High workload for placement staff, reducing focus on interview prep and student guidance.

With companies expecting fast and high-quality shortlists, an **automated, scalable, and consistent system** is required.

---

## Objective
The Automated Resume Relevance Check System aims to:
- Automate resume evaluation against job requirements at scale.
- Provide actionable feedback to students.
- Maintain a searchable database of evaluations for the placement team.

---

## Sample Data
You can download sample data [here](#).

---

## Proposed Solution
We propose an **AI-powered resume evaluation engine** that combines:
1. **Rule-based checks** (keyword/skill matching).
2. **LLM-based semantic understanding**.

### Features:
- Accept resumes (PDF/DOCX) uploaded by students.
- Accept job descriptions uploaded by the placement team.
- Extract text, normalize formats, and parse sections.
- Perform **hard match** (keywords, skills, education) and **semantic match** (embeddings + LLM reasoning).
- Generate **Relevance Score, Missing Elements, and Verdict**.
- Store results in a searchable web dashboard.

---

## Workflow

1. **Job Requirement Upload**
   - Placement team uploads job descriptions (JD).

2. **Resume Upload**
   - Students upload resumes while applying.

3. **Resume Parsing**
   - Extract text from PDF/DOCX.
   - Standardize formats (remove headers/footers, normalize sections).

4. **JD Parsing**
   - Extract role title, must-have skills, good-to-have skills, and qualifications.

5. **Relevance Analysis**
   - **Hard Match:** Keyword & skill check (exact and fuzzy matches).
   - **Semantic Match:** Embedding similarity between resume and JD using LLMs.
   - **Scoring & Verdict:** Weighted scoring formula for final score.

6. **Output Generation**
   - Relevance Score (0–100).
   - Missing Skills/Projects/Certifications.
   - Verdict (High / Medium / Low suitability).
   - Suggestions for student improvement.

7. **Storage & Access**
   - Results stored in the database.
   - Placement team can search/filter resumes by job role, score, and location.

8. **Web Application**
   - Placement team dashboard to upload JD and view shortlisted resumes.

---

## Tech Stack

### Core Resume Parsing, AI & Scoring
- **Python** – Primary programming language.
- **PDF/DOCX Parsing:** `PyMuPDF`, `pdfplumber`, `python-docx`, `docx2txt`
- **NLP:** `spaCy`, `NLTK`
- **LLM Orchestration:** `LangChain`, `LangGraph`, `LangSmith`
- **Vector Stores:** `Chroma`, `FAISS`, `Pinecone`
- **LLM Models:** OpenAI GPT, Gemini, Claude, HuggingFace models
- **Keyword Matching:** TF-IDF, BM25, fuzzy matching
- **Semantic Matching:** Embeddings + cosine similarity
- **Scoring:** Weighted combination of hard and soft matches

### Web Application
- **Backend:** Flask / FastAPI – API to process uploads, run evaluation, and serve results
- **Frontend (MVP):** Streamlit – Dashboard for upload and review
- **Database:** SQLite / PostgreSQL – Stores results, metadata, and audit logs

---

## Features
- Automated resume evaluation with **speed and accuracy**.
- Provides **personalized improvement feedback** for students.
- **Searchable dashboard** for placement teams.
- Handles **thousands of resumes weekly**.
- Combines **hard keyword checks** with **contextual semantic understanding**.

---

## Installation & Setup

```bash
# Clone repository
git clone https://github.com/sonyvakode/resume-relevance-check.git
cd resume-relevance-check

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
