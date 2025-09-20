def compute_score(text):
    return min(100, max(0, len(text.split()) // 5))

def get_verdict(score):
    if score >= 80:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"

def get_missing_skills(resume_text, jd_id=None):
    dummy_skills = ["Python", "SQL", "Machine Learning", "Communication"]
    return [s for s in dummy_skills if s.lower() not in resume_text.lower()]

def get_improvement_suggestions(resume_text, jd_id=None):
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
