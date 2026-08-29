# ============================================================
# TYPE HINTS IN PYTHON
# PART 2: LIST TYPE HINTS
# ============================================================


# ============================================================
# 1. LIST OF INTEGERS
# ============================================================

numbers: list[int] = [10, 20, 30]


# list[int] means:
#
# numbers is expected to be a list containing integers.
#
# Example:
#
# [10, 20, 30]       -> correct
# [100, 200, 300]    -> correct
#
# ["10", "20", "30"] -> not the expected type


# ============================================================
# 2. FUNCTION WITH A LIST TYPE HINT
# ============================================================

def total(numbers: list[int]) -> int:
    return sum(numbers)


# Read this as:
#
# numbers -> list containing integers
# return  -> integer
#
# Example:
#
# total([10, 20, 30])
#
# returns:
#
# 60


# ============================================================
# 3. LIST OF STRINGS
# ============================================================

def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello", name)


# list[str] means:
#
# names is expected to be a list containing strings.
#
# Example:
#
# names = ["Alice", "John", "Bob"]


# ============================================================
# 4. FOR LOOP WITH A LIST
# ============================================================

names: list[str] = ["Alice", "John", "Bob"]

greet_all(names)


# Output:
#
# Hello Alice
# Hello John
# Hello Bob
#
#
# The loop:
#
# for name in names:
#
# takes one item from the list during each iteration.
#
# Iteration 1:
# name = "Alice"
#
# Iteration 2:
# name = "John"
#
# Iteration 3:
# name = "Bob"


# ============================================================
# 5. WHAT DOES -> None MEAN?
# ============================================================

def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello", name)


# -> None means:
#
# The function is expected to return None.
#
# In simple terms:
#
# The function does not return a useful value.
#
# Instead, it performs an action:
#
#     print("Hello", name)


# ============================================================
# 6. CHECKING THE RETURN VALUE
# ============================================================

result = greet_all(["Alice", "Bob"])

print(result)


# Output:
#
# Hello Alice
# Hello Bob
# None


# Why does None appear?
#
# Because the function does not have:
#
# return something
#
# When a Python function reaches the end without returning
# a value, Python automatically returns None.


# ============================================================
# 7. IMPORTANT: -> None VS return None
# ============================================================

# -> None is a TYPE HINT.
#
# It tells us what the function is expected to return.


def example() -> None:
    print("Hello")


# There is no explicit return statement.
#
# Python automatically returns None.


# You can also explicitly write:
#
# return None
#
# Example:


def example_explicit() -> None:
    print("Hello")
    return None


# Both functions return None.


# ============================================================
# 8. IMPORTANT LIST TYPE HINTS
# ============================================================

numbers: list[int] = [1, 2, 3]

names: list[str] = ["Alice", "John"]

prices: list[float] = [10.5, 20.75, 99.99]

flags: list[bool] = [True, False, True]


# Quick reference:
#
# list[int]   -> list of integers
# list[str]   -> list of strings
# list[float] -> list of decimal numbers
# list[bool]  -> list of True/False values


# ============================================================
# 9. QUICK SUMMARY
# ============================================================

# Variable:
#
# names: list[str] = ["Alice", "John", "Bob"]


# Function parameter:
#
# def greet_all(names: list[str]):


# Return type:
#
# def greet_all(names: list[str]) -> None:


# Complete function:
#
# def greet_all(names: list[str]) -> None:
#     for name in names:
#         print("Hello", name)


# Remember:
#
# list[str]
#     -> list containing strings
#
# list[int]
#     -> list containing integers
#
# -> None
#     -> function returns None
#        (no useful return value)


# ============================================================
# KEY IDEA
# ============================================================
#
# Type hints describe what kind of data we EXPECT.
#
# They help:
#     - IDEs
#     - Linters
#     - Static type checkers
#     - Developers
#
# Python does not automatically enforce these hints at runtime.
# ============================================================