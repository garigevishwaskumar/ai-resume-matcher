import streamlit as st
from utils import match_resume_jd

st.set_page_config(page_title="AI Resume Matcher", layout="centered")

st.title("🤖 AI Resume–Job Matcher")
st.write("Upload resume and paste job description")

resume_text = st.text_area("📄 Paste Resume Text")
jd_text = st.text_area("🧾 Paste Job Description")

if st.button("Analyze"):
    if resume_text and jd_text:
        score, skills = match_resume_jd(resume_text, jd_text)

        st.success(f"✅ Match Score: {score}%")

        st.subheader("📌 Extracted Skills")
        st.write(skills[:20])

        st.subheader("🧠 AI Insight")
        st.write(
            "This resume shows good alignment with the job description. "
            "Improving missing technical skills can further increase the match score."
        )
    else:
        st.warning("Please enter both Resume and Job Description.")
