import sys
from pathlib import Path
from datetime import datetime
import streamlit as st

# Safe imports
PROJECT_ROOT = Path(__file__).parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from utils import parser, scorer, storage

st.set_page_config(page_title="ARRCS", layout="wide", page_icon="📊")

def render_header():
    st.markdown("<h1 style='text-align:center'>🧠 Automated Resume Relevance Check System</h1>", unsafe_allow_html=True)

def render_navigation():
    col1, col2, col3, col4 = st.columns(4)
    nav_items = [("📊","Dashboard","dashboard"), ("📤","Upload","upload"), ("👥","Jobs","jobs"), ("📋","Results","results")]
    selected_tab = st.session_state.get('selected_tab','dashboard')
    for i,(icon,label,key) in enumerate(nav_items):
        col=[col1,col2,col3,col4][i]
        with col:
            if st.button(f"{icon}\n{label}", key=f"nav_{key}", use_container_width=True):
                st.session_state.selected_tab = key
                st.rerun()

# Dashboard metrics
def render_metrics():
    evals = storage.list_evaluations()
    jds = storage.list_jds()
    col1,col2,col3,col4=st.columns(4)
    with col1: st.metric("Total Resumes Processed", len(evals))
    with col2: st.metric("Weekly Job Requirements", len(jds))
    with col3: st.metric("Avg Processing Time", "24s")
    with col4: st.metric("High Quality Matches", len([e for e in evals if e.get('score',0)>=80]))

def render_dashboard():
    render_metrics()
    col1,col2=st.columns(2)
    with col1:
        if st.button("Upload New Batch of Resumes"):
            st.session_state.selected_tab='upload'
            st.rerun()
    with col2:
        if st.button("Create New Job Posting"):
            st.session_state.selected_tab='jobs'
            st.rerun()

# Upload resumes
def render_upload_section():
    st.subheader("📤 Upload Resumes")
    uploaded_files = st.file_uploader("Select resumes", accept_multiple_files=True)
    jd_id = st.text_input("Associated Job ID")
    if st.button("Process Upload") and uploaded_files and jd_id:
        for file in uploaded_files:
            resume_text = parser.extract_text(file)
            score = scorer.compute_score(resume_text)
            verdict = scorer.get_verdict(score)
            missing_skills = scorer.get_missing_skills(resume_text, jd_id)
            suggestions = scorer.get_improvement_suggestions(resume_text, jd_id)
            storage.add_evaluation({
                "jd_id": jd_id,
                "candidate": file.name,
                "score": score,
                "verdict": verdict,
                "missing_skills": missing_skills,
                "suggestions": suggestions,
                "timestamp": str(datetime.now())
            })
        st.success(f"{len(uploaded_files)} resumes processed successfully!")

# Jobs
def render_jobs_section():
    st.subheader("👥 Job Postings")
    job_title = st.text_input("Job Title")
    location = st.text_input("Location")
    jd_id = st.text_input("Job ID")
    if st.button("Create Job Posting") and job_title and jd_id:
        storage.add_jd({"id": jd_id, "title": job_title, "location": location, "timestamp": str(datetime.now())})
        st.success(f"Job '{job_title}' created successfully!")

# Results
def render_results_section():
    st.subheader("📋 Evaluation Results")
    evals = storage.list_evaluations()
    jds = {jd["id"]: jd for jd in storage.list_jds()}
    if not evals: st.info("No evaluations yet."); return

    col1,col2,col3=st.columns(3)
    with col1: min_score = st.slider("Minimum Score",0,100,0)
    with col2: verdict_filter = st.selectbox("Verdict", ["All","High","Medium","Low"])
    with col3:
        locations = sorted({jd.get("location") for jd in jds.values() if jd.get("location")})
        loc_filter = st.selectbox("Location", ["All"] + locations)

    filtered = evals
    if min_score>0: filtered = [e for e in filtered if e.get('score',0)>=min_score]
    if verdict_filter!="All": filtered = [e for e in filtered if e.get('verdict')==verdict_filter]
    if loc_filter!="All": filtered = [e for e in filtered if jds.get(e.get('jd_id'), {}).get('location')==loc_filter]

    for e in filtered[:50]:
        jd = jds.get(e.get('jd_id'), {})
        st.markdown(f"""
        **Candidate:** {e.get('candidate')}  
        **Job:** {jd.get('title','N/A')} | **Location:** {jd.get('location','N/A')}  
        **Relevance Score:** {e.get('score')}  
        **Verdict:** {e.get('verdict')}  
        **Missing Skills:** {', '.join(e.get('missing_skills',[]))}  
        **Improvement Suggestions:** {', '.join(e.get('suggestions',[]))}
        """)
        st.write("---")

# Main
def main():
    if 'selected_tab' not in st.session_state: st.session_state.selected_tab='dashboard'
    render_header()
    render_navigation()
    tab = st.session_state.get('selected_tab','dashboard')
    if tab=='dashboard': render_dashboard()
    elif tab=='upload': render_upload_section()
    elif tab=='jobs': render_jobs_section()
    elif tab=='results': render_results_section()

if __name__=="__main__":
    main()
