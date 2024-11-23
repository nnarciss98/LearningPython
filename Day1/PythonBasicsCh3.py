3# Chapter 3 - Functions

# 1. Function Definitions
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# 2. Using Default Arguments
def introduce(name, age=30):
    print(f"Hi, I'm {name}, and I'm {age} years old.")

introduce("Bob")  # Output: Hi, I'm Bob, and I'm 30 years old.
introduce("Charlie", 25)  # Output: Hi, I'm Charlie, and I'm 25 years old.

# 3. Using *args (Variable-Length Arguments)
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: 10
print(add_numbers(5, 10, 15))  # Output: 30

# 4. Using **kwargs (Variable-Length Keyword Arguments)
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=25, job="Developer")
# Output:
# name: Alice
# age: 25
# job: Developer

# 5. Functions as Arguments
def multiply(x):
    return x * x

def apply_function(f, value):
    return f(value)

print(apply_function(multiply, 5))  # Output: 25

# 6. Combining Functions with *args and **kwargs
def combine_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

combine_args_kwargs(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}

# 7. Lambda Functions for Simple Operations
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

# Example: Using a lambda function for a filter operation
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Example: Using a lambda function for sorting a list of tuples
data = [('Bob', 75), ('Alice', 90), ('Eve', 85)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [('Bob', 75), ('Eve', 85), ('Alice', 90)]

# 8. Function with a Scope
x = 10  # Global variable

def modify_global_var():
    global x  # Access and modify the global variable inside the function
    x = 20

modify_global_var()
print(x)  # Output: 20

# 9. Functions Returning Multiple Values
def get_user_details():
    return "Alice", 25, "Developer"

name, age, job = get_user_details()
print(name)  # Output: Alice
print(age)   # Output: 25
print(job)   # Output: Developer

# 10. Passing Functions as Arguments
def square(x):
    return x ** 2

def apply_function_to_value(func, value):
    return func(value)

print(apply_function_to_value(square, 4))  # Output: 16

# Example: Applying different functions based on a condition
def double(x):
    return x * 2

def halve(x):
    return x / 2

def apply_operation(func, value):
    return func(value)

print(apply_operation(double, 5))  # Output: 10
print(apply_operation(halve, 10))  # Output: 5.0

# Example: Sorting using a custom key
students = [("John", 85), ("Emma", 92), ("Sophia", 88)]
sorted_students = sorted(students, key=lambda student: student[1])  # Sort by score
print(sorted_students)  # Output: [('John', 85), ('Sophia', 88), ('Emma', 92)]
