# JSON to Schema Converter

The JSON to Schema Converter is a Python script that takes a JSON file as input and generates a schema that outlines the structure of the JSON data. This schema includes information about the data types and example values for each field, making it easier to understand the structure and content of complex JSON files.

## Technical Details

The script is written in Python and uses the built-in `json` and `argparse` modules. It works by recursively traversing the JSON object and generating a corresponding schema object. The script can handle JSON objects, arrays, and primitive data types.

- For JSON objects, it generates a schema object with a "properties" field.
- For JSON arrays, it generates a schema object with an "items" field.
- For primitive data types (e.g., integers, strings), it generates a schema object with "type" and "example" fields.

The "type" field in the schema can be optionally included or excluded based on a command line argument.

## Usage

1. Make sure you have Python installed on your system. You can download it from [the official Python website](https://www.python.org/).
2. Save the script as `json_2_schema.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using the following command:

   ```
   python json_2_schema.py <path_to_json_file> [--include-type]
   ```

    - Replace `<path_to_json_file>` with the path to your JSON file.
    - Include `--include-type` if you want the schema to include "type" information.

## Examples

1. **Generate Schema without Type Information:**
   ```bash
   python json_2_schema.py data/vendor-list.json
   ```

   Output:
   ```json
   {
     "properties": {
       "gvlSpecificationVersion": {
         "example": 42
       },
       ...
     }
   }
   ```

2. **Generate Schema with Type Information:**
   ```bash
   python json_2_schema.py data/vendor-list.json --include-type
   ```

   Output:
   ```json
   {
     "type": "object",
     "properties": {
       "gvlSpecificationVersion": {
         "type": "int",
         "example": 42
       },
       ...
     }
   }
   ```

In both examples, the output is a JSON schema printed to the console. You can redirect the output to a file using `>` if you want to save it. For example:

```bash
python json_2_schema.py data/vendor-list.json > output.json
```
