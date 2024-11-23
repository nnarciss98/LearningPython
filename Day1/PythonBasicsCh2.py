# Chapter 2: Flow Control

# 1. Boolean Values and Comparison Operators
print(5 == 5)  # True
print(3 < 4)   # True
print(5 != 5)  # False

# 2. The if Statement
age = 20
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult.")
else:
    print("You are an adult.")  # Output: You are an adult.

# 3. Nested if Statements
age = 20
if age >= 18:
    if age >= 21:
        print("You are 21 or older.")
    else:
        print("You are an adult but not 21.")  # Output: You are an adult but not 21.

# 4. Boolean Logic: and, or, not
x = 5
if x > 3 and x < 10:
    print("x is between 3 and 10")  # Output: x is between 3 and 10

# 5. The while Loop
i = 0
while i < 5:
    print(i)
    i += 1  # Output: 0, 1, 2, 3, 4

# 6. The for Loop
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Using for loop with lists
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry

# 7. break, continue, and pass

# break: Exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0, 1, 2, 3, 4

# continue: Skip the current iteration
for i in range(5):
    if i == 3:
        continue
    print(i)  # Output: 0, 1, 2, 4

# pass: Placeholder that does nothing
if False:
    pass  # No action taken

# Example containing both break and continue in the same code block for more complex flow control:
# Outer loop
for i in range(5):
    print(f"Outer loop iteration {i}")

    # Inner loop
    for j in range(5):
        if j == 2:
            print("  Skipping inner loop iteration when j == 2")
            continue  # Skips when j == 2

        if i == 3 and j == 4:
            print("  Breaking out of both loops when i == 3 and j == 4")
            break  # Breaks out of the inner loop

        print(f"  Inner loop iteration {j}")

    # Break out of the outer loop if inner loop ends early
    if i == 3:
        break  # Exits outer loop completely when i == 3

