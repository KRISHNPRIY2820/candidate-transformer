from pydantic import BaseModel
from typing import List, Optional


class Skill(BaseModel):
    name: str
    confidence: float
    sources: List[str]


class Experience(BaseModel):
    company: str
    title: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    summary: Optional[str] = None


class Education(BaseModel):
    institution: str
    degree: Optional[str] = None
    field: Optional[str] = None
    end_year: Optional[int] = None


class CandidateProfile(BaseModel):
    candidate_id: str
    full_name: Optional[str] = None
    emails: List[str] = []
    phones: List[str] = []
    location: Optional[dict] = None

    links: dict = {
        "linkedin": None,
        "github": None,
        "portfolio": None,
        "other": []
    }

    headline: Optional[str] = None
    years_experience: Optional[float] = None

    skills: List[Skill] = []
    experience: List[Experience] = []
    education: List[Education] = []

    provenance: List[dict] = []
    overall_confidence: float = 0.0
