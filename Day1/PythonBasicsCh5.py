# Chapter 5: Dictionaries

# 1. Creating Dictionaries
phone_book = {"Alice": "1234", "Bob": "5678"}
empty_dict = {}  # Empty dictionary
mixed_dict = {"name": "Alice", "age": 25, "friends": ["Bob", "Charlie"]}

# 2. Accessing Dictionary Values
print(phone_book["Alice"])  # Accessing value by key, Output: 1234
print(phone_book.get("Charlie", "Not Found"))  # Using get(), Output: Not Found

# 3. Modifying Dictionaries
# Changing values
phone_book["Alice"] = "4321"
# Adding new key-value pair
phone_book["David"] = "1122"
# Removing items using del
del phone_book["Bob"]
# Removing item and returning value using pop()
value = phone_book.pop("Alice")
print(value)  # Output: 4321

# 4. Dictionary Methods
# keys(), values(), items()
print(phone_book.keys())    # Output: dict_keys(['David'])
print(phone_book.values())  # Output: dict_values(['1122'])
print(phone_book.items())   # Output: dict_items([('David', '1122')])

# update() to add or update key-value pairs
phone_book.update({"Eve": "3345"})
print(phone_book)  # Output: {'David': '1122', 'Eve': '3345'}

# copy() to create a shallow copy of the dictionary
phone_book_copy = phone_book.copy()
print(phone_book_copy)  # Output: {'David': '1122', 'Eve': '3345'}

# 5. Nested Dictionaries
address_book = {
    "Alice": {"address": "123 Main St", "phone": "1234"},
    "Bob": {"address": "456 Elm St", "phone": "5678"}
}
print(address_book["Alice"]["address"])  # Output: 123 Main St

# 6. Iterating Over Dictionaries
# Iterating through keys
for name in phone_book:
    print(name)  # Output: David, Eve

# Iterating through values
for number in phone_book.values():
    print(number)  # Output: 1122, 3345

# Iterating through key-value pairs
for name, number in phone_book.items():
    print(f"{name}: {number}")  # Output: David: 1122, Eve: 3345

# 7. Dictionary Comprehensions
# Creating dictionary with dictionary comprehension
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
