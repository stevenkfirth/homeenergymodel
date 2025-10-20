import os
import json

import jsonschema


def apply_schema_validation(project_dict):
    fhs_schema = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FHS_schema.json")
    with open(fhs_schema, "r") as schema_file:
        schema = json.load(schema_file)
    validator = jsonschema.Draft7Validator(schema)
    errors = sorted(validator.iter_errors(project_dict), key=lambda error: error.path)
    if errors:
        combined_error_msg = "\n".join(f"{list(error.path)}: {error.message}" for error in errors)
        raise ValueError(f"FHS input validation failed:\n{combined_error_msg}")
