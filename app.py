import streamlit as st
from resume_parser import extract_text
from ai_analyzer import analyze_resume
import google.generativeai as genai
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get AI-powered analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume Uploaded Successfully")

    resume_text = extract_text(uploaded_file)

    with st.expander("View Extracted Resume Text"):
        st.write(resume_text)

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(resume_text)

        st.subheader("Analysis Result")
        st.write(result)
