# Automating the boring stuff with Python
# Chapter 1: Python Basics

# 1. Installing Python
# Install from https://python.org and run Python from terminal using 'python' or 'python3'.

# 2. Running Python Code
# Interactive shell:
# python
# >>> 2 + 2
# >>> 5 * 5

# Running a script:
# Save the code in a .py file, for example: script.py
# Run in terminal: python script.py

# 3. Core Data Types

# Integers and Floats:
int_num = 5  # Integer
float_num = 3.14  # Float
print(int_num + float_num)  # Output: 8.14

# Strings:
str_example = "Hello, Python!"
print(str_example)  # Output: Hello, Python!

# 4. Variables and Assignment
name = "Alice"
age = 25
print(name, age)  # Output: Alice 25

# 5. Input and Output

# Print Statement:
print("Hello, World!")  # Output: Hello, World!

# Taking User Input:
user_name = input("Enter your name: ")  # User enters a name
print("Hello, " + user_name)  # Output: Hello, [user's name]

# 6. Comments
# This is a single-line comment
print("Comments are ignored by Python.")  # This prints a message

# 7. Errors and Debugging
# SyntaxError Example: Uncomment the next line to see the error
# print(Hello)  # NameError: Hello is not defined

# 8. Practice: Basic Python Script
# A simple program to greet the user
user_name = input("What is your name? ")
print("Hello, " + user_name + "!")  # Output: Hello, [user's name]!
