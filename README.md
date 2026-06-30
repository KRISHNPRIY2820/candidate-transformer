# Candidate Transformer

## Problem

Transforms candidate information from multiple sources into a single canonical profile.

## Sources Implemented

### Structured
- ATS JSON
- Recruiter CSV

### Unstructured
- Recruiter Notes TXT
- Resume TXT

## Features

- Canonical schema
- Phone normalization (E.164)
- Skill canonicalization
- Conflict resolution
- Confidence scoring
- Provenance tracking
- Runtime configurable projection layer
- Validation
- CLI interface

## Installation

pip install -r requirements.txt

## Run Default Output

python main.py \
--ats data/ats.json \
--csv data/recruiter.csv \
--notes data/notes.txt \
--config configs/default.json

## Run Custom Output

python main.py \
--ats data/ats.json \
--csv data/recruiter.csv \
--notes data/notes.txt \
--config configs/custom.json

## Run Tests

pytest

## Output Files

outputs/default_output.json
outputs/custom_output.json
outputs/full_output.json
