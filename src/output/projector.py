import json


def get_nested(
        obj,
        path):

    if path.endswith("[0]"):

        field = path.replace(
            "[0]",
            ""
        )

        arr = obj.get(field, [])

        if len(arr) > 0:
            return arr[0]

        return None

    return obj.get(path)


def project(
        profile,
        config_path):

    with open(
            config_path,
            "r",
            encoding="utf-8") as f:

        config = json.load(f)

    output = {}

    on_missing = config.get(
        "on_missing",
        "null"
    )

    for field in config["fields"]:

        target = field["path"]

        source_path = field.get(
            "from",
            target
        )

        value = get_nested(
            profile,
            source_path
        )

        if value is None:

            if on_missing == "omit":
                continue

            if on_missing == "error":
                raise ValueError(
                    f"Missing {target}"
                )

            output[target] = None

        else:

            output[target] = value

    if config.get(
            "include_confidence",
            False):

        output["overall_confidence"] = (
            profile.get(
                "overall_confidence"
            )
        )

    return output
