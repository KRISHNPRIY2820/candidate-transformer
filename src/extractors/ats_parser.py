import json


def parse_ats(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return {
            "full_name": data.get("candidateName"),
            "emails": [data.get("candidateEmail")],
            "phones": [data.get("candidatePhone")],
            "company": data.get("currentOrg"),
            "title": data.get("designation"),
            "skills": data.get("skills", []),
            "source": "ats"
        }

    except Exception:
        return {}
