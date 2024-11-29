# Chapter 10: Debugging

import logging
import pdb

# 1. Using Assertions
x = -1
assert x > 0, "x must be positive"  # AssertionError if False

# 2. Using Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

logging.disable(logging.CRITICAL)  # Disable all critical-level logs and below

# 3. Debugging with pdb
def faulty_function(a, b):
    pdb.set_trace()  # Set breakpoint
    return a / b

try:
    result = faulty_function(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

# 4. Exception Handling
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Caught error: {e}")
finally:
    print("This always runs")
