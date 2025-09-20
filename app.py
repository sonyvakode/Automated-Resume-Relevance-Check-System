import streamlit as st
from pathlib import Path
from datetime import datetime
import sys

# Add utils folder to path for safe imports
current_dir = Path(__file__).parent
sys.path.append(str(current_dir / "utils"))

import parser as parser_module
import scorer as scorer_module
import storage as storage_module

# ==================== Page Config ====================
st.set_page_config(
    page_title="ARRCS - AI Resume Screening",
    layout="wide",
    page_icon="📊"
)

# ==================== Header ====================
def render_header():
    st.markdown('''
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="color: #2d3748;">🧠 Automated Resume Relevance Check System</h1>
    </div>
    ''', unsafe_allow_html=True)

# ==================== Navigation ====================
def render_navigation():
    col1, col2, col3, col4 = st.columns(4)
    nav_items = [("📊","Dashboard","dashboard"),
                 ("📤","Upload","upload"),
                 ("👥","Jobs","jobs"),
                 ("📋","Results","results")]
    selected_tab = st.session_state.get('selected_tab','dashboard')
    for i,(icon,label,key) in enumerate(nav_items):
        col=[col1,col2,col3,col4][i]
        with col:
            if st.button(f"{icon}\n{label}", key=f"nav_{key}", use_container_width=True):
                st.session_state.selected_tab=key
                st.rerun()

# ==================== Dashboard ====================
def render_metrics():
    evals = storage_module.list_evaluations()
    jds = storage_module.list_jds()
    total_resumes = len(evals)
    active_jobs = len(jds)
    high_quality_matches = len([e for e in evals if e.get('score',0)>=80])
    avg_processing_time="24s"
    
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Total Resumes Processed", total_resumes)
    with col2:
        st.metric("Weekly Job Requirements", active_jobs)
    with col3:
        st.metric("Avg Processing Time", avg_processing_time)
    with col4:
        st.metric("High Quality Matches", high_quality_matches)

def render_dashboard():
    render_metrics()
    st.write("Quick Actions")
    col1,col2=st.columns(2)
    with col1:
        if st.button("Upload New Batch of Resumes"):
            st.session_state.selected_tab='upload'
            st.rerun()
    with col2:
        if st.button("Create New Job Posting"):
            st.session_state.selected_tab='jobs'
            st.rerun()

# ==================== Upload Resumes ====================
def render_upload_section():
    st.subheader("📤 Upload Resumes")
    uploaded_files = st.file_uploader("Select resumes (PDF/DOCX)", accept_multiple_files=True)
    jd_id = st.text_input("Associated Job ID")
    if st.button("Process Upload") and uploaded_files and jd_id:
        for file in uploaded_files:
            text = parser_module.extract_text(file)
            score = scorer_module.compute_score(text)
            verdict = scorer_module.get_verdict(score)
            missing = scorer_module.get_missing_skills(text, jd_id)
            suggestions = scorer_module.get_improvement_suggestions(text, jd_id)
            storage_module.add_evaluation({
                "jd_id": jd_id,
                "candidate": file.name,
                "score": score,
                "verdict": verdict,
                "missing_skills": missing,
                "suggestions": suggestions,
                "timestamp": str(datetime.now())
            })
        st.success(f"{len(uploaded_files)} resumes processed successfully!")

# ==================== Jobs ====================
def render_jobs_section():
    st.subheader("👥 Job Postings")
    job_title = st.text_input("Job Title")
    location = st.text_input("Location")
    jd_id = st.text_input("Job ID (Unique)")
    if st.button("Create Job Posting") and job_title and jd_id:
        storage_module.add_jd({
            "id": jd_id,
            "title": job_title,
            "location": location,
            "timestamp": str(datetime.now())
        })
        st.success(f"Job '{job_title}' created successfully!")

# ==================== Results ====================
def render_results_section():
    st.subheader("📋 Evaluation Results")
    evals = storage_module.list_evaluations()
    jds = {jd["id"]: jd for jd in storage_module.list_jds()}

    col1, col2, col3 = st.columns(3)
    with col1:
        min_score = st.slider("Minimum Score", 0, 100, 0)
    with col2:
        verdict_filter = st.selectbox("Verdict", ["All", "High", "Medium", "Low"])
    with col3:
        locations = sorted({jd.get("location") for jd in jds.values() if jd.get("location")})
        loc_filter = st.selectbox("Location", ["All"] + locations)

    filtered = evals
    if min_score > 0:
        filtered = [e for e in filtered if e.get("score", 0) >= min_score]
    if verdict_filter != "All":
        filtered = [e for e in filtered if e.get("verdict") == verdict_filter]
    if loc_filter != "All":
        filtered = [e for e in filtered if jds.get(e.get("jd_id"), {}).get("location") == loc_filter]

    for e in filtered[:50]:
        jd = jds.get(e.get("jd_id"), {})
        st.write(f"**{e.get('candidate')}** | Score: {e.get('score'):.1f} | Verdict: {e.get('verdict')} | Job: {jd.get('title','N/A')} | Location: {jd.get('location','N/A')}")
        st.write(f"**Missing Skills:** {e.get('missing_skills')}")
        st.write(f"**Improvement Suggestions:** {e.get('suggestions')}")
        st.markdown("---")

# ==================== Main ====================
def main():
    if 'selected_tab' not in st.session_state:
        st.session_state.selected_tab='dashboard'
    render_header()
    render_navigation()
    tab = st.session_state.get('selected_tab','dashboard')
    if tab == 'dashboard':
        render_dashboard()
    elif tab == 'upload':
        render_upload_section()
    elif tab == 'jobs':
        render_jobs_section()
    elif tab == 'results':
        render_results_section()

if __name__ == "__main__":
    main()
