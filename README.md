# Candidate Transformer

## Problem

Transforms candidate information from multiple sources into a single canonical profile.

## Sources Implemented

### Structured Sources
- ATS JSON
- Recruiter CSV

### Unstructured Sources
- Recruiter Notes TXT
- Resume TXT

## Features

- Canonical candidate schema
- Phone normalization (E.164)
- Skill canonicalization
- Conflict resolution
- Confidence scoring
- Provenance tracking
- Runtime configurable projection layer
- Validation
- CLI interface

## Installation

```bash
pip install -r requirements.txt
```

## Run Default Output

```bash
python main.py \
--ats data/ats.json \
--csv data/recruiter.csv \
--notes data/notes.txt \
--config configs/default.json
```

## Run Custom Output

```bash
python main.py \
--ats data/ats.json \
--csv data/recruiter.csv \
--notes data/notes.txt \
--config configs/custom.json
```

## Run Tests

```bash
pytest
```

## Output Files

- outputs/default_output.json
- outputs/custom_output.json
- outputs/full_output.json
