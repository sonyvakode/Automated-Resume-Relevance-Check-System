import json
from pathlib import Path

# ==================== File Paths ====================
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
EVAL_FILE = DATA_DIR / "evaluations.json"
JD_FILE = DATA_DIR / "jds.json"

# Initialize files if they don't exist
for file in [EVAL_FILE, JD_FILE]:
    if not file.exists():
        file.write_text("[]")

# ==================== Evaluations ====================
def list_evaluations():
    """Return list of all stored evaluations"""
    with open(EVAL_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def add_evaluation(evaluation: dict):
    """Add a new resume evaluation"""
    evals = list_evaluations()
    evals.append(evaluation)
    with open(EVAL_FILE, "w", encoding="utf-8") as f:
        json.dump(evals, f, indent=4)

# ==================== Job Descriptions ====================
def list_jds():
    """Return list of all stored job postings"""
    with open(JD_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def add_jd(jd: dict):
    """Add a new job posting"""
    jds = list_jds()
    jds.append(jd)
    with open(JD_FILE, "w", encoding="utf-8") as f:
        json.dump(jds, f, indent=4)
