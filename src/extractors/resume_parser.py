import re


def parse_resume(path):

    try:

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        phones = re.findall(
            r"\d{10}",
            text
        )

        skills = []

        for skill in [
            "python",
            "machine learning",
            "sql"
        ]:
            if skill in text.lower():
                skills.append(skill)

        return {
            "emails": emails,
            "phones": phones,
            "skills": skills,
            "source": "resume"
        }

    except Exception:
        return {}
