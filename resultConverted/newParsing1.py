import json

# Load the JSON data from the file
with open('done_01_中醫名詞大辭典.json', 'r') as json_file:
    data = json.load(json_file)

# Process each dictionary in the list
for entry in data:
    # Remove the "tag" key
    if "tag" in entry:
        del entry["tag"]
    
    # Update "instruction" using the value from "input"
    if "input" in entry:
        entry["instruction"] = entry.pop("input")
    
    # Set "input" to an empty string
    entry["input"] = ""

# Save the modified data back to the file
with open('new_results_01.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
