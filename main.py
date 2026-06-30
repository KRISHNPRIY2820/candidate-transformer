import json
import re
from pathlib import Path

# ------------------------
# CONFIG
# ------------------------

SOURCE_CONFIDENCE = {
    "ats": 0.95,
    "notes": 0.85
}

SKILL_MAP = {
    "python": "Python",
    "ml": "Machine Learning",
    "machine learning": "Machine Learning",
    "sql": "SQL"
}

# ------------------------
# ATS PARSER
# ------------------------

def parse_ats(path):

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return {
        "full_name": data.get("candidateName"),
        "emails": [data.get("candidateEmail")],
        "phones": [data.get("candidatePhone")],
        "skills": data.get("skills", []),
        "source": "ats"
    }

# ------------------------
# NOTES PARSER
# ------------------------

def parse_notes(path):

    text = Path(path).read_text(encoding="utf-8")

    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    phone = re.findall(
        r"\d{10}",
        text
    )

    skills = []

    for skill in SKILL_MAP.keys():
        if skill in text.lower():
            skills.append(skill)

    return {
        "emails": email,
        "phones": phone,
        "skills": skills,
        "source": "notes"
    }

# ------------------------
# NORMALIZATION
# ------------------------

def normalize_skills(skills):

    result = []

    for skill in skills:

        skill = skill.lower()

        if skill in SKILL_MAP:
            result.append(SKILL_MAP[skill])

        else:
            result.append(skill.title())

    return sorted(list(set(result)))

# ------------------------
# MERGE
# ------------------------

def merge_records(records):

    output = {
        "candidate_id": "CAND001",
        "full_name": None,
        "emails": [],
        "phones": [],
        "skills": [],
        "provenance": []
    }

    best_name_score = -1

    for r in records:

        score = SOURCE_CONFIDENCE[r["source"]]

        if r.get("full_name") and score > best_name_score:

            output["full_name"] = r["full_name"]
            best_name_score = score

            output["provenance"].append({
                "field": "full_name",
                "source": r["source"],
                "confidence": score
            })

        output["emails"].extend(r.get("emails", []))
        output["phones"].extend(r.get("phones", []))
        output["skills"].extend(r.get("skills", []))

    output["emails"] = sorted(list(set(output["emails"])))
    output["phones"] = sorted(list(set(output["phones"])))
    output["skills"] = normalize_skills(output["skills"])

    output["overall_confidence"] = round(
        sum(SOURCE_CONFIDENCE.values()) /
        len(SOURCE_CONFIDENCE),
        2
    )

    return output

# ------------------------
# MAIN
# ------------------------

if __name__ == "__main__":

    ats = parse_ats("data/ats.json")

    notes = parse_notes(
        "data/recruiter_notes.txt"
    )

    final_record = merge_records(
        [ats, notes]
    )

    print(
        json.dumps(
            final_record,
            indent=4
        )
    )
