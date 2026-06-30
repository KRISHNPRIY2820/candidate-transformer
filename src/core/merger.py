from src.normalizers.phone import normalize_phone
from src.normalizers.skill import canonicalize_skills
from src.core.confidence import get_source_confidence
from src.core.provenance import create_provenance


def merge_records(records):

    profile = {
        "candidate_id": "CAND001",

        "full_name": None,

        "emails": [],
        "phones": [],

        "location": None,

        "links": {
            "linkedin": None,
            "github": None,
            "portfolio": None,
            "other": []
        },

        "headline": None,

        "years_experience": None,

        "skills": [],

        "experience": [],
        "education": [],

        "provenance": []
    }

    best_name_conf = -1

    all_conf = []

    for record in records:

        if not record:
            continue

        source = record.get("source")

        conf = get_source_confidence(source)

        all_conf.append(conf)

        if record.get("full_name"):

            if conf > best_name_conf:

                profile["full_name"] = record["full_name"]

                best_name_conf = conf

                profile["provenance"].append(
                    create_provenance(
                        "full_name",
                        source,
                        "highest_confidence"
                    )
                )

        profile["emails"].extend(
            record.get("emails", [])
        )

        profile["phones"].extend(
            record.get("phones", [])
        )

        profile["skills"].extend(
            record.get("skills", [])
        )

    profile["emails"] = sorted(
        list(
            set(
                [
                    e.lower().strip()
                    for e in profile["emails"]
                    if e
                ]
            )
        )
    )

    profile["phones"] = sorted(
        list(
            set(
                [
                    normalize_phone(p)
                    for p in profile["phones"]
                    if normalize_phone(p)
                ]
            )
        )
    )

    skills = canonicalize_skills(
        profile["skills"]
    )

    profile["skills"] = [
        {
            "name": skill,
            "confidence": 0.9,
            "sources": [
                "merged"
            ]
        }
        for skill in skills
    ]

    profile["overall_confidence"] = round(
        sum(all_conf) / len(all_conf),
        2
    )

    return profile
