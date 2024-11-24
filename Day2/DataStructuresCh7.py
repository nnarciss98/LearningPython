import re

# 1. Regular Expressions - Literal Characters
print(re.match("hello", "hello world"))  # Matches "hello" at the start

# 2. Dot (.) Character - Matches any character except newline
print(re.match("a.b", "acb"))  # Matches "acb"

# 3. Character Sets [ ] - Matches any character in the set
print(re.match("[aeiou]", "a"))  # Matches vowel
print(re.match("[0-9]", "5"))    # Matches a digit

# 4. Ranges - Matches a range of characters
print(re.match("[a-z]", "b"))  # Matches lowercase letter

# 5. Negation (^) - Matches characters not in the set
print(re.match("[^0-9]", "a"))  # Matches non-digit character

# 6. Predefined Character Classes
print(re.match(r"\d", "3"))   # Matches digit
print(re.match(r"\w", "abc")) # Matches word character (letters, digits, _)
print(re.match(r"\s", " "))   # Matches whitespace

# 7. Quantifiers - Specify occurrences
print(re.match(r"ab*", "abbbb"))  # Matches "ab" followed by zero or more "b"s
print(re.match(r"ab+", "abbb"))   # Matches "ab" followed by one or more "b"s
print(re.match(r"ab?", "ab"))     # Matches "ab" followed by zero or one "b"

# 8. re.match() vs re.search()
print(re.match("hello", "hello world"))  # Matches at the start of the string
print(re.search("world", "hello world"))  # Matches anywhere in the string

# 9. re.findall() - Find all non-overlapping matches
print(re.findall(r"\d+", "123 abc 456"))  # Output: ['123', '456']

# 10. re.finditer() - Iterate over matches
for match in re.finditer(r"\d+", "123 abc 456"):
    print(match.group())  # Output: 123, 456

# 11. Groups and Capturing
match = re.search(r"(\d+)\s+(\w+)", "123 abc")
print(match.group(0))  # Output: 123 abc (entire match)
print(match.group(1))  # Output: 123 (first group)
print(match.group(2))  # Output: abc (second group)

# 12. Non-capturing Groups
print(re.match(r"(?:abc)+", "abcabcabc"))  # Matches without capturing

# 13. re.sub() - Substituting text
print(re.sub(r"world", "Python", "hello world"))  # Output: hello Python

# 14. Flags in Regular Expressions
print(re.search(r"hello", "HELLO world", re.IGNORECASE))  # Case-insensitive match

# 15. re.split() - Splitting a string by a pattern
print(re.split(r"\s+", "Hello    World   Python"))  # Output: ['Hello', 'World', 'Python']
