import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

EVAL_FILE = DATA_DIR / "evaluations.json"
JD_FILE = DATA_DIR / "jds.json"

def _load(file):
    if file.exists():
        return json.loads(file.read_text())
    return []

def _save(file, data):
    file.write_text(json.dumps(data, indent=2))

def add_evaluation(evaluation):
    data = _load(EVAL_FILE)
    data.append(evaluation)
    _save(EVAL_FILE, data)

def list_evaluations():
    return _load(EVAL_FILE)

def add_jd(jd):
    data = _load(JD_FILE)
    data.append(jd)
    _save(JD_FILE, data)

def list_jds():
    return _load(JD_FILE)
