import json
from pathlib import Path

DB_FILE = Path(__file__).parent.parent / "data/evaluations.json"
JD_FILE = Path(__file__).parent.parent / "data/sample_jds.json"

def _load(file):
    if not file.exists():
        return []
    with open(file, "r") as f:
        return json.load(f)

def _save(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def list_evaluations():
    return _load(DB_FILE)

def add_evaluation(record):
    data = _load(DB_FILE)
    data.append(record)
    _save(DB_FILE, data)

def list_jds():
    return _load(JD_FILE)

def add_jd(record):
    data = _load(JD_FILE)
    data.append(record)
    _save(JD_FILE, data)
