from src.core.canonical_model import (
    CandidateProfile
)


def validate_profile(profile):

    CandidateProfile(
        **profile
    )

    return True
