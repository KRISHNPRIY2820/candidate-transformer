SKILL_MAP = {
    "python": "Python",
    "py": "Python",

    "ml": "Machine Learning",
    "machine learning": "Machine Learning",

    "sql": "SQL",

    "deep learning": "Deep Learning"
}


def canonicalize_skills(skills):

    result = []

    for skill in skills:

        skill = skill.strip().lower()

        if skill in SKILL_MAP:
            result.append(SKILL_MAP[skill])

        else:
            result.append(skill.title())

    return sorted(list(set(result)))
