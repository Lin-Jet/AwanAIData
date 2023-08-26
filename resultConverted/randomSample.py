import json
import random

print("File to sample: ")
inputfile = input()
print("Name sampled file: ")
outputfilename = input()

# Load the JSON data
with open(f'{inputfile}.json', 'r') as file:
    json_data = json.load(file)

# Define the number of random samples to select
num_samples = 30

# Get the total number of samples in the JSON data
total_samples = len(json_data)

# Randomly select sample indices
random_indices = random.sample(range(total_samples), num_samples)

# Create a list to store the selected samples
selected_samples = []

# Retrieve the selected samples from the JSON data
for index in random_indices:
    selected_samples.append(json_data[index])

# Create a new JSON object with the selected samples
output_data = selected_samples

# Save the selected samples to a new JSON file
with open(f'{outputfilename}.json', 'w') as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)
