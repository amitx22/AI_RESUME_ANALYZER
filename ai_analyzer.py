import google.generativeai as genai
model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_resume(resume_text):

    prompt = f"""
    Analyze this resume and provide:

    1. Resume Score out of 100
    2. Skills Identified
    3. Strengths
    4. Weaknesses
    5. Suggestions for Improvement
    6. Suitable Job Roles

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    return response.text
