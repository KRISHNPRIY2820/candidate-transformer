from src.core.merger import merge_records


def test_merge():

    records = [
        {
            "full_name": "Priyanshi",
            "emails": [
                "a@gmail.com"
            ],
            "source": "ats"
        }
    ]

    result = merge_records(
        records
    )

    assert (
        result["full_name"]
        == "Priyanshi"
    )
