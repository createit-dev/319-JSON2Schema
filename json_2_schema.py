import json

def get_json_schema(json_obj):
    if isinstance(json_obj, dict):
        if not json_obj:  # Empty dict
            return {"type": "object", "properties": {}}
        first_key, first_item = next(iter(json_obj.items()))
        if all(isinstance(value, type(first_item)) for value in json_obj.values()) and first_key.isdigit():
            return {first_key: get_json_schema(first_item)}
        else:
            schema = {"type": "object", "properties": {}}
            for key, value in json_obj.items():
                schema["properties"][key] = get_json_schema(value)
            return schema
    elif isinstance(json_obj, list):
        if not json_obj:  # Empty list
            return {"type": "array", "items": {}}
        return {"type": "array", "items": get_json_schema(json_obj[0])}
    else:
        return {"type": str(type(json_obj).__name__)}

def main():
    with open('data/vendor-list.json', 'r') as f:
        data = json.load(f)

    schema = get_json_schema(data)
    print(json.dumps(schema, indent=2))

if __name__ == "__main__":
    main()
