import argparse
import json

from src.extractors.ats_parser import parse_ats
from src.extractors.csv_parser import parse_csv
from src.extractors.notes_parser import parse_notes
# from src.extractors.resume_parser import parse_resume
from src.extractors.resume_parser import parse_resume
from src.core.merger import merge_records
from src.core.validator import validate_profile

from src.output.projector import project


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--ats"
    )

    parser.add_argument(
        "--csv"
    )

    parser.add_argument(
        "--notes"
    )
    parser.add_argument(
    "--resume"
    )

    parser.add_argument(
        "--config",
        required=True
    )

    args = parser.parse_args()

    records = []

    if args.ats:
        records.append(
            parse_ats(args.ats)
        )

    if args.csv:
        records.append(
            parse_csv(args.csv)
        )

    if args.notes:
        records.append(
            parse_notes(args.notes)
        )
    if args.resume:
        records.append(
            parse_resume(args.resume)
        )

    profile = merge_records(
        records
    )

    validate_profile(
        profile
    )

    output = project(
        profile,
        args.config
    )

    print(
        json.dumps(
            output,
            indent=4
        )
    )


if __name__ == "__main__":
    main()
