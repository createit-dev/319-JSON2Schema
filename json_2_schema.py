import json
import argparse

def get_json_schema(json_obj, include_type=True):
    if isinstance(json_obj, dict):
        if not json_obj:  # Empty dict
            return {"type": "object", "properties": {}} if include_type else {"properties": {}}
        first_key, first_item = next(iter(json_obj.items()))
        if all(isinstance(value, type(first_item)) for value in json_obj.values()) and first_key.isdigit():
            return {first_key: get_json_schema(first_item, include_type)}
        else:
            schema = {"type": "object", "properties": {}} if include_type else {"properties": {}}
            for key, value in json_obj.items():
                schema["properties"][key] = get_json_schema(value, include_type)
            return schema
    elif isinstance(json_obj, list):
        if not json_obj:  # Empty list
            return {"type": "array", "items": {}} if include_type else {"items": {}}
        return {"type": "array", "items": get_json_schema(json_obj[0], include_type)} if include_type else {"items": get_json_schema(json_obj[0], include_type)}
    else:
        return {"type": str(type(json_obj).__name__), "example": json_obj} if include_type else {"example": json_obj}

def main():
    parser = argparse.ArgumentParser(description='Generate a JSON schema from a JSON file.')
    parser.add_argument('filename', help='The JSON file to analyze')
    parser.add_argument('--include-type', action='store_true', help='Include type information in the schema')
    args = parser.parse_args()

    with open(args.filename, 'r') as f:
        data = json.load(f)

    schema = get_json_schema(data, args.include_type)
    print(json.dumps(schema, indent=2))

if __name__ == "__main__":
    main()
