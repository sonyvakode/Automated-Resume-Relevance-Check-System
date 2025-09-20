from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_hard_match_score(resume_text, jd_text, keywords=[]):
    """Simple keyword match score (0-100)"""
    resume_lower = resume_text.lower()
    matched = sum(1 for kw in keywords if kw.lower() in resume_lower)
    if not keywords:
        return 0
    return round((matched / len(keywords)) * 100, 2)

def calculate_semantic_score(resume_text, jd_text):
    """Semantic similarity using TF-IDF + cosine similarity"""
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)

def calculate_final_score(hard_score, semantic_score, hard_weight=0.5, semantic_weight=0.5):
    """Weighted combination of hard and semantic scores"""
    return round(hard_score * hard_weight + semantic_score * semantic_weight, 2)

def get_verdict(score):
    """Return High / Medium / Low based on score"""
    if score >= 75:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"
