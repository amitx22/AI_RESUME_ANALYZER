import streamlit as st
from resume_parser import extract_text, get_resume_details
from ai_analyzer import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ================= CSS =================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

.main {
    background-color: #0f172a;
}

.hero {
    text-align:center;
    padding:25px;
    border-radius:15px;
    background:linear-gradient(135deg,#0ea5e9,#2563eb);
    color:white;
    margin-bottom:20px;
}

.hero h1{
    font-size:50px;
    margin-bottom:5px;
}

.hero p{
    font-size:18px;
}

.card{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    color:white;
    box-shadow:0px 0px 10px rgba(0,0,0,0.3);
}

.result-box{
    background:#111827;
    color:white;
    padding:25px;
    border-radius:15px;
    border-left:6px solid #38bdf8;
    line-height:1.8;
}

.stButton>button{
    width:100%;
    height:55px;
    font-size:18px;
    font-weight:bold;
    border:none;
    border-radius:12px;
    background:linear-gradient(90deg,#06b6d4,#2563eb);
    color:white;
}

.stButton>button:hover{
    transform:scale(1.02);
}

.metric-card{
    background:#1e293b;
    padding:15px;
    border-radius:12px;
    text-align:center;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ================= HERO =================

st.markdown("""
<div class="hero">
<h1>📄 AI Resume Analyzer</h1>
<p>Analyze Resume with Gemini AI & Get Professional Career Insights</p>
</div>
""", unsafe_allow_html=True)

# ================= STATS =================

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="metric-card">
    <h3>⚡ Fast</h3>
    AI Powered Analysis
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
    <h3>🎯 Accurate</h3>
    Skills Detection
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
    <h3>🚀 Career Ready</h3>
    Job Suggestions
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ================= MAIN SECTION =================

col1,col2 = st.columns([1,1])

with col1:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    st.subheader("📂 Upload Resume")

    uploaded_file = st.file_uploader(
        "Choose PDF Resume",
        type=["pdf"]
    )

    st.markdown("</div>",unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">
    <h3>✨ Features</h3>

    ✅ Resume Score

    ✅ Skills Extraction

    ✅ Strengths Analysis

    ✅ Weakness Detection

    ✅ Improvement Suggestions

    ✅ Suitable Job Roles

    ✅ ATS Optimization Tips

    </div>
    """, unsafe_allow_html=True)

# ================= ANALYSIS =================

if uploaded_file:

    st.success("✅ Resume Uploaded Successfully")

    resume_text = extract_text(uploaded_file)

    with st.expander("📜 Resume Preview"):
        st.write(resume_text)

    if st.button("🚀 Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(resume_text)

        st.success("Analysis Completed")

        st.markdown("## 📊 Analysis Report")

        st.markdown(
            f"""
            <div class="result-box">
            {result}
            </div>
            """,
            unsafe_allow_html=True
        )

# ================= FOOTER =================

st.markdown("---")

st.markdown("""
<center>
Made with ❤️ using Streamlit + Gemini AI
</center>
""", unsafe_allow_html=True)
