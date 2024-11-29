# Chapter 13: Automating CSV and JSON Handling

import csv
import json
from datetime import datetime

# ------------------- CSV Handling -------------------

# Reading a CSV File
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list

# Writing to a CSV File
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])  # Write header
    writer.writerow(['Alice', 30, 'New York'])  # Write data row

# Reading CSV into Dictionaries
with open('example.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age'])  # Access by column name

# Writing CSV from Dictionaries
with open('output_dict.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write header
    writer.writerow({'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'})

# ------------------- JSON Handling -------------------

# Parsing a JSON String
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)
print(data['name'], data['age'])  # Access JSON as dictionary

# Loading JSON from a File
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data['name'])

# Writing JSON to a File
output_data = {'name': 'Bob', 'age': 25}
with open('output.json', 'w') as file:
    json.dump(output_data, file, indent=4)  # Pretty format with indent

# Converting Python Object to JSON String
json_str = json.dumps(output_data)
print(json_str)

# Handling Nested JSON Data
nested_data = {'user': {'name': 'Alice', 'details': {'age': 30}}}
print(nested_data['user']['details']['age'])  # Access nested data

# Custom JSON Serialization for Non-Serializable Objects
def date_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

custom_data = {'timestamp': datetime.now()}
json_custom = json.dumps(custom_data, default=date_handler)
print(json_custom)
