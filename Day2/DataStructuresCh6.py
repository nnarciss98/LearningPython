# Chapter 6: Manipulating Strings

# 1. Escape Characters
print("Hello\nWorld!")  # Newline, Output: Hello (newline) World!
print("He said, \"Hello!\"")  # Output: He said, "Hello!"

# 2. Raw Strings
print(r"C:\path\to\file")  # Output: C:\path\to\file

# 3. Multiline Strings
multiline = """This is
a multiline
string."""
print(multiline)

# 4. String Indexing and Slicing
name = "Python"
print(name[0])   # First character, Output: P
print(name[-1])  # Last character, Output: n
print(name[0:3]) # Slice, Output: Pyt

# 5. String Methods
print("hello".upper())    # Convert to uppercase, Output: HELLO
print("WORLD".lower())    # Convert to lowercase, Output: world
print("hello".isupper())  # Check if uppercase, Output: False
print("Hello".startswith("He"))  # Output: True
print("Hello".endswith("lo"))    # Output: True

# join() and split()
print(", ".join(["a", "b", "c"]))  # Combine list, Output: a, b, c
print("a, b, c".split(", "))      # Split string, Output: ['a', 'b', 'c']

# rjust(), ljust(), center()
print("Hello".rjust(10))   # Output: '     Hello'
print("Hello".ljust(10))   # Output: 'Hello     '
print("Hello".center(10))  # Output: '  Hello   '

# strip(), lstrip(), rstrip()
print("   Hello   ".strip())       # Remove whitespace, Output: 'Hello'
print("www.example.com".strip("w."))  # Remove specific chars, Output: 'example.com'

# 6. String Formatting
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old.")  # f-string
print("My name is {} and I'm {} years old.".format(name, age))  # format()

# 7. Finding and Replacing
print("Hello World".find("World"))  # Find substring, Output: 6
print("Hello World".replace("World", "Python"))  # Replace substring, Output: Hello Python

# 8. Checking String Characteristics
print("Hello".isalpha())  # Check if letters only, Output: True
print("123".isdecimal())  # Check if numbers only, Output: True
print("   ".isspace())    # Check if spaces only, Output: True
