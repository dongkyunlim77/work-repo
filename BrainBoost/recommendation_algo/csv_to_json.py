import csv
import json

# Specify your input CSV file and output JSON file.
input_csv = "pokemon.csv"      # Replace with your CSV file name.
output_json = "descriptors.json"    # Output JSON file.
meta_json = "meta_descriptors.json"    # Output JSON file.


data = []
types_set = set()

# Open the CSV file. Change delimiter="\t" to delimiter="," if needed.
with open(input_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        name = row["Name"].strip()
        type1 = row["Type1"].strip()
        type2 = row["Type2"].strip()
        data.append((name, type1, type2))
        # Add non-empty type values to the set.
        if type1:
            types_set.add(type1)
        if type2:
            types_set.add(type2)

# Create a sorted list of unique types and a mapping from type to index.
types_list = sorted(list(types_set))
type_to_index = {t: i for i, t in enumerate(types_list)}
index_to_type = {i: t for i, t in enumerate(types_list)}
with open(meta_json, "w", encoding='utf-8') as f:
    json.dump(index_to_type, f, indent=4)

# Create a multi-hot encoding for each image.
json_data = {}
num_types = len(types_list)

for name, type1, type2 in data:
    one_hot = [0] * num_types
    if type1:
        index = type_to_index[type1]
        one_hot[index] = 1
    if type2:
        index = type_to_index[type2]
        one_hot[index] = 1
    json_data[name] = one_hot

# Write the resulting mapping to a JSON file.
with open(output_json, "w", encoding='utf-8') as f:
    json.dump(json_data, f, indent=4)

print(f"Conversion complete! JSON file saved as {output_json}")
