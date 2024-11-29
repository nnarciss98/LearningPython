# File Handling in Python

import os
import shelve

# 1. Reading Files
with open('example.txt', 'r') as file:
    content = file.read()  # Reads the entire file
    print(content)

with open('example.txt', 'r') as file:
    for line in file:  # Reads line by line
        print(line.strip())  # Removes newline characters

# 2. Writing to Files
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")  # Overwrites the file

with open('example.txt', 'a') as file:
    file.write("Appending new content.\n")  # Appends to the file

# 3. Working with File Paths
print(os.path.abspath('example.txt'))  # Get absolute path
print(os.path.exists('example.txt'))  # Check if file exists

# 4. Binary Files
# Writing binary data
with open('binaryfile.bin', 'wb') as file:
    file.write(b'\x00\x01\x02')

# Reading binary data
with open('binaryfile.bin', 'rb') as file:
    data = file.read()
    print(data)  # Output: b'\x00\x01\x02'

# 5. Exception Handling
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# 6. Using Shelve for Persistent Storage
with shelve.open('mydata') as shelf:
    shelf['key'] = {'a': 1, 'b': 2}  # Store a dictionary

with shelve.open('mydata') as shelf:
    print(shelf['key'])  # Output: {'a': 1, 'b': 2}
