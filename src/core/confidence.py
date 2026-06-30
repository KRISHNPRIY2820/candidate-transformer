SOURCE_WEIGHTS = {
    "ats": 0.95,
    "csv": 0.90,
    "notes": 0.70
}


def get_source_confidence(source):

    return SOURCE_WEIGHTS.get(
        source,
        0.50
    )
