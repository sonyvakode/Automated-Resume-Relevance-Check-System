import json
from pathlib import Path

# Database files
DB_FILE = Path(__file__).parent.parent / "data" / "evaluations.json"
JD_FILE = Path(__file__).parent.parent / "data" / "jds.json"

def _ensure_dir(file_path):
    """Ensure folder exists for the file path."""
    file_path.parent.mkdir(parents=True, exist_ok=True)

def _save(file, data):
    _ensure_dir(file)
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

def _load(file):
    if not file.exists():
        return []
    with open(file, "r") as f:
        return json.load(f)

# ------------------ Evaluations ------------------
def list_evaluations():
    return _load(DB_FILE)

def add_evaluation(evaluation):
    data = _load(DB_FILE)
    data.append(evaluation)
    _save(DB_FILE, data)

# ------------------ Job Descriptions ------------------
def list_jds():
    return _load(JD_FILE)

def add_jd(jd):
    data = _load(JD_FILE)
    data.append(jd)
    _save(JD_FILE, data)
