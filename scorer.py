# ==================== Scoring and Suggestions ====================
def compute_score(text):
    """Dummy scoring function: returns 0-100 relevance score."""
    return min(100, max(0, len(text.split()) // 5))  # simple word-count-based score

def get_verdict(score):
    if score >= 80:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"

def get_missing_skills(resume_text, jd_id=None):
    """Dummy missing skills detection"""
    dummy_skills = ["Python", "SQL", "Machine Learning", "Communication"]
    missing = [s for s in dummy_skills if s.lower() not in resume_text.lower()]
    return missing

def get_improvement_suggestions(resume_text, jd_id=None):
    """Dummy improvement suggestions"""
    suggestions = []
    if "internship" not in resume_text.lower():
        suggestions.append("Add relevant internship experience")
    if "project" not in resume_text.lower():
        suggestions.append("Include projects to showcase skills")
    if "certification" not in resume_text.lower():
        suggestions.append("Add certifications if any")
    if not suggestions:
        suggestions.append("Keep improving experience and skills")
    return suggestions
