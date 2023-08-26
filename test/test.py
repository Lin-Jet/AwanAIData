import re

file = open("rawData_02_formulaNote-繁體.txt", "r")
lines = file.readlines()
file.close()

segments = []  # Move segments list declaration outside of the if block

lines_iterator = iter(lines)  # Convert lines list into an iterator

for line in lines_iterator:
    boundary = re.search(r"#===", line)
    if boundary:
        segment = []  # Initialize a new segment
        while boundary is not None:  # Check if the search result is not None
            segment.append(line)
            # Read the next line
            line = next(lines_iterator, None)
            if line:
                boundary = re.search(r"#===", line)
            else:
                boundary = None
        segments.append(segment)  # Append the segment to the list of segments

# Print the content between the segments
for segment in segments:
    for line in segment[1:-1]:  # Exclude the boundary lines
        print(line)

