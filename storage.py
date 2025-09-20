import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)
EVAL_FILE = DATA_DIR / "evaluations.json"
JD_FILE = DATA_DIR / "jds.json"

# ==================== Helper ====================
def load_json(file_path):
    if file_path.exists():
        with open(file_path,"r",encoding="utf-8") as f:
            return json.load(f)
    return []

def save_json(file_path,data):
    with open(file_path,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)

# ==================== Evaluations ====================
def list_evaluations():
    return load_json(EVAL_FILE)

def add_evaluation(evaluation):
    data = load_json(EVAL_FILE)
    data.append(evaluation)
    save_json(EVAL_FILE,data)

# ==================== Job Postings ====================
def list_jds():
    return load_json(JD_FILE)

def add_jd(jd):
    data = load_json(JD_FILE)
    data.append(jd)
    save_json(JD_FILE,data)
