from PyPDF2 import PdfReader
import re

def extract_text(pdf_file):
    """
    Extract text and basic resume information from PDF
    """

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def get_resume_details(pdf_file):
    """
    Extract resume details
    """

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    # Email Extraction
    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    # Phone Number Extraction
    phones = re.findall(
        r"\+?\d[\d\s\-]{8,15}",
        text
    )

    # Common Skills
    skills_list = [
        "Python",
        "Java",
        "C++",
        "C",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "Machine Learning",
        "Deep Learning",
        "Data Science",
        "Git",
        "GitHub",
        "MongoDB",
        "MySQL",
        "AWS",
        "Azure",
        "Docker"
    ]

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return {
        "text": text,
        "pages": len(reader.pages),
        "word_count": len(text.split()),
        "emails": emails,
        "phones": phones,
        "skills": found_skills
    }
