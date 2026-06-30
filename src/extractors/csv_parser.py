import pandas as pd


def parse_csv(path):
    try:
        df = pd.read_csv(path)

        row = df.iloc[0]

        return {
            "full_name": row["name"],
            "emails": [row["email"]],
            "phones": [str(row["phone"])],
            "company": row["current_company"],
            "title": row["title"],
            "source": "csv"
        }

    except Exception:
        return {}
