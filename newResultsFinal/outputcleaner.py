import json


print("File to clean: ")
inputfile = input()
print("Name cleaned file: ")
outputfilename = input()


def is_invalid_output(output):
    return output.endswith(":") or output.endswith(": 。") or output.endswith(":。") or output.endswith("可應用在。") or output.endswith("是出自論的方劑。") or output.endswith("的功用是。")

# Read the JSON file
with open(f"{inputfile}.json", "r") as file:
    data = json.load(file)

# Filter entries
filtered_data = [entry for entry in data if not is_invalid_output(entry["output"])]

# Write the filtered data back to a new JSON file
with open(f"{outputfilename}.json", "w") as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=4)
