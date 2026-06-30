import json

def project(record, config_path):

    with open(config_path) as f:
        config = json.load(f)

    output = {}

    for field in config["fields"]:

        key = field["path"]

        output[key] = record.get(key)

    return output
