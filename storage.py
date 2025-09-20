import json
from pathlib import Path

DB_EVAL = Path("data/evaluations.json")
DB_JD = Path("data/jds.json")

def _load(file):
    if file.exists():
        with open(file,"r") as f:
            return json.load(f)
    return []

def _save(file, data):
    with open(file,"w") as f:
        json.dump(data,data,f,indent=4)

def list_evaluations():
    return _load(DB_EVAL)

def add_evaluation(record):
    data = _load(DB_EVAL)
    data.append(record)
    _save(DB_EVAL,data)

def list_jds():
    return _load(DB_JD)

def add_jd(record):
    data = _load(DB_JD)
    data.append(record)
    _save(DB_JD,data)
