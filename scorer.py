from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def normalize_text(s):
    s = s or ""
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def extract_skills_from_jd(jd_text, top_k=40):
    text = jd_text or ""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    candidates = []
    for line in lines:
        if "skill" in line.lower() or "requirements" in line.lower() or "," in line:
            parts = re.split(r"[,:;•\-]", line)
            for p in parts:
                p = p.strip()
                if len(p) > 1 and len(p.split()) <= 6:
                    candidates.append(p)
    if not candidates:
        tokens = re.findall(r"\b[a-zA-Z\+\#\-\_]{2,}\b", text.lower())
        freq = {}
        for t in tokens:
            freq[t] = freq.get(t,0)+1
        sorted_tokens = sorted(freq.items(), key=lambda x:-x[1])
        candidates = [t for t,_ in sorted_tokens[:top_k]]
    seen = set(); out = []
    for c in candidates:
        key = c.lower()
        if key not in seen:
            out.append(c)
            seen.add(key)
    return out[:top_k]

def hard_match_score(resume_text, jd_skills):
    resume = normalize_text(resume_text)
    score = 0.0
    matches = []
    for skill in jd_skills:
        s = normalize_text(skill)
        if s and s in resume:
            score += 1.0
            matches.append((skill, 1.0))
    if jd_skills:
        return 100.0 * (score / len(jd_skills)), matches
    return 0.0, matches

def semantic_score(resume_text, jd_text):
    texts = [resume_text, jd_text]
    vectorizer = TfidfVectorizer(stop_words="english", max_features=2000)
    try:
        tfidf = vectorizer.fit_transform(texts)
        sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        return float(sim) * 100.0
    except Exception:
        return 0.0

def score_resume_against_jd(resume_text, jd_text):
    resume_text = normalize_text(resume_text)
    jd_text = normalize_text(jd_text)
    jd_skills = extract_skills_from_jd(jd_text)
    hard_score, hard_matches = hard_match_score(resume_text, jd_skills)
    soft_score = semantic_score(resume_text, jd_text)
    final = 0.6 * hard_score + 0.4 * soft_score
    missing = [s for s in jd_skills if normalize_text(s) not in resume_text]
    matches = sorted(hard_matches, key=lambda x: -x[1])
    verdict = "Low"
    if final >= 70: verdict = "High"
    elif final >= 40: verdict = "Medium"
    return {"final_score": final, "hard_score": hard_score, "soft_score": soft_score, "missing": missing, "matches": matches, "verdict": verdict}
