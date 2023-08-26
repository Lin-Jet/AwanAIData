import json
import glob

# Specify the path pattern for the input JSON files
json_files = glob.glob("./*.json")

# Create an empty list to store the merged contents
merged_data = []

# Iterate over each JSON file
for file_path in json_files:
    with open(file_path, "r", encoding="utf-8") as file:
        # Load the JSON contents
        data = json.load(file)
        # Extend the merged_data list with the loaded JSON contents
        merged_data.extend(data)

# Write the merged contents to a new JSON file
output_file = "benchmarkSamples.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(merged_data, file, ensure_ascii=False, indent=4)

print(f"Merged JSON files saved to {output_file}")
