import json
from pathlib import Path

DB_FILE = Path("resume_evaluations.json")

def save_evaluation(resume_name, job_title, score, verdict, missing_skills=[]):
    """Save evaluation to JSON file"""
    if DB_FILE.exists():
        with open(DB_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    entry = {
        "resume_name": resume_name,
        "job_title": job_title,
        "score": score,
        "verdict": verdict,
        "missing_skills": missing_skills
    }
    data.append(entry)

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_evaluations():
    """Load all evaluations from JSON file"""
    if DB_FILE.exists():
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []
