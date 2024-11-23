import copy
# Chapter 4: Lists

# 1. Creating Lists
fruits = ["apple", "banana", "cherry"]
empty_list = []
mixed_list = [1, "apple", 3.14, ["nested", "list"]]

# 2. Indexing and Accessing List Items
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry
print(fruits[1:3])  # Output: ['banana', 'cherry']

# 3. Modifying Lists
# Changing Elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding Items
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

fruits.insert(1, "pear")  # Adds "pear" at index 1
print(fruits)  # Output: ['apple', 'pear', 'blueberry', 'cherry', 'orange']

fruits.extend(["kiwi", "melon"])
print(fruits)  # Output: ['apple', 'pear', 'blueberry', 'cherry', 'orange', 'kiwi', 'melon']

# Removing Items
fruits.remove("banana")  # Removes first occurrence of "banana"
print(fruits)  # Output: ['apple', 'pear', 'blueberry', 'cherry', 'orange', 'kiwi', 'melon']

fruits.pop(1)  # Removes the item at index 1
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange', 'kiwi', 'melon']

# Clearing List
fruits.clear()
print(fruits)  # Output: []

# 4. List Methods and Functions
# List Length
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3

# Check if Item Exists
print("apple" in fruits)  # Output: True

# Sorting Lists
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Reversing Lists
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']

# Copying Lists
# Original list with nested list (a mutable object)
original_list = [1, 2, [3, 4], 5]

# Create a shallow copy using the copy() method
shallow_copy = original_list.copy()

# Modify an element in the nested list of the shallow copy
shallow_copy[2][0] = 99

print("Original List:", original_list)  # Output: [1, 2, [99, 4], 5]
print("Shallow Copy:", shallow_copy)    # Output: [1, 2, [99, 4], 5]

# Create a deep copy using the deepcopy() function
deep_copy = copy.deepcopy(original_list)

# Modify an element in the nested list of the deep copy
deep_copy[2][0] = 77

print("Original List:", original_list)  # Output: [1, 2, [99, 4], 5]
print("Deep Copy:", deep_copy)          # Output: [1, 2, [77, 4], 5]


# 5. Nested Lists
nested_list = [1, [2, 3, 4], 5]
print(nested_list[1][2])  # Output: 4

# 6. List Comprehensions
# Basic Example
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# List Comprehension with Condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

# 7. Important List Functions
numbers = [3, 1, 4, 1, 5, 9]
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 9
print(sum(numbers))  # Output: 23
