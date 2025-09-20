from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_hard_match_score(resume_text: str, jd_text: str, keywords: list = []) -> float:
    """
    Calculate hard skill match score (0-100) based on keyword presence.
    
    Parameters:
    - resume_text: str, candidate's resume text
    - jd_text: str, job description text
    - keywords: list of strings, key skills to match
    
    Returns:
    - score: float, 0-100
    """
    if not resume_text or not keywords:
        return 0.0
    resume_lower = resume_text.lower()
    matched = sum(1 for kw in keywords if kw.lower() in resume_lower)
    score = (matched / len(keywords)) * 100
    return round(min(score, 100.0), 2)

def calculate_semantic_score(resume_text: str, jd_text: str) -> float:
    """
    Calculate semantic similarity between resume and job description
    using TF-IDF vectorization + cosine similarity.
    
    Returns:
    - score: float, 0-100
    """
    if not resume_text or not jd_text:
        return 0.0
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)

def calculate_final_score(hard_score: float, semantic_score: float, hard_weight: float = 0.5, semantic_weight: float = 0.5) -> float:
    """
    Combine hard match and semantic scores into a final weighted score.
    
    Returns:
    - final_score: float, 0-100
    """
    final = hard_score * hard_weight + semantic_score * semantic_weight
    return round(min(max(final, 0), 100), 2)

def get_verdict(score: float) -> str:
    """
    Return verdict based on score thresholds.
    """
    if score >= 75:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"
