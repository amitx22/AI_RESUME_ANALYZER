import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text):

    prompt = f"""
You are a professional ATS Resume Reviewer.

Analyze the resume and provide:

# Resume Score (0-100)

# ATS Score (0-100)

# Skills Identified

# Strengths

# Weaknesses

# Missing Skills

# Suggestions for Improvement

# Suitable Job Roles

# Interview Preparation Tips

Resume:
{resume_text}
"""

    response = model.generate_content(prompt)

    return response.text

