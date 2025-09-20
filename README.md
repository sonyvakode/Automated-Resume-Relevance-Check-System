# Automated Resume Relevance Check System (MVP)

This is an MVP for the **Automated Resume Relevance Check System** designed for placement teams.
Sure! Here’s a complete **README.md** tailored for your **Automated Resume Relevance Check System (ARRCS)** project with instructions, features, and setup details:

```markdown
# 🧠 Automated Resume Relevance Check System (ARRCS)

ARRCS is an AI-powered system to automatically evaluate resumes against job postings. It provides a **Relevance Score**, missing skills/projects/certifications, and verdicts (High/Medium/Low suitability). The system also stores results in a database for easy search and filtering by placement teams.

---

## 🌟 Features

- **Resume Evaluation**
  - Computes **Relevance Score (0–100)**
  - Identifies **missing skills, projects, certifications**
  - Provides **Verdict** (High / Medium / Low)
  - Suggestions for **candidate improvement**
- **Job Management**
  - Add new job postings with **title, location, and job ID**
- **Dashboard**
  - Displays total resumes processed, weekly job requirements, high-quality matches, and average processing time
- **Results Storage & Filtering**
  - Stores evaluation results in a **JSON database**
  - Filter/search results by **score, verdict, job location**
- **User-friendly UI**
  - Built with **Streamlit**
  - Supports **upload of multiple resumes (PDF, DOCX, TXT)**

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – UI framework
- **PyPDF2** – PDF resume parsing
- **python-docx** – DOCX resume parsing
- **pandas** – Data handling
- **JSON** – Simple storage for resumes and job postings

---

## 📂 Project Structure

```

automated\_resume\_relevance\_checker/
├── app.py                  # Main Streamlit application
├── utils/
│   ├── **init**.py
│   ├── parser.py           # Resume text extraction
│   ├── scorer.py           # Resume scoring logic
│   └── storage.py          # JSON database handling
├── data/
│   ├── evaluations.json    # Stored evaluation results
│   └── jds.json            # Stored job postings
├── requirements.txt        # Required Python packages
└── README.md

````

---

## ⚡ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/automated_resume_relevance_checker.git
cd automated_resume_relevance_checker
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit PyPDF2 python-docx pandas
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

4. **Open in browser**
   The app will automatically open at `http://localhost:8501`.

---

## 📝 Usage

1. **Dashboard**

   * View metrics like total resumes processed, active jobs, high-quality matches.

2. **Upload Resumes**

   * Upload multiple resumes (PDF, DOCX, TXT)
   * Associate each with a Job ID
   * Scores and verdicts are computed automatically

3. **Jobs**

   * Add new job postings with `Job ID`, `Job Title`, and `Location`

4. **Results**

   * Filter resumes by:

     * Minimum Score
     * Verdict (High / Medium / Low)
     * Location
   * View candidate name, score, verdict, job title, and location

---

## 📌 Notes

* Ensure **PyPDF2** and **python-docx** are installed for PDF/DOCX support
* All data is stored in JSON files (`data/evaluations.json` and `data/jds.json`) for simplicity
* You can expand `scorer.py` to include **missing skills/projects/certifications analysis** using AI/ML models

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit changes (`git commit -m "Add feature"`)
5. Push to branch (`git push origin feature-name`)
6. Create a Pull Request

---

## 📄 License

MIT License. See `LICENSE` file for details.

---

```

If you want, I can also create a **ready `requirements.txt`** and a **minimal JSON DB template** so your app is plug-and-play.  

Do you want me to do that next?
```
