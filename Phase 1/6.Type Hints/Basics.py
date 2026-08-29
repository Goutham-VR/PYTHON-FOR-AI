# ============================================================
# TYPE HINTS IN PYTHON
# ============================================================
#
# Type hints tell developers and tools what types of values
# a variable, function parameter, or return value is expected
# to have.
#
# IMPORTANT:
# Type hints are NOT automatically enforced by Python.
# They are mainly useful for:
#   - IDEs
#   - Linters
#   - Static type checkers such as mypy
#   - Developers reading and maintaining code
# ============================================================


# ============================================================
# 1. BASIC SYNTAX
# ============================================================

# Variable type hints

age: int = 25

name: str = "Alice"

price: float = 99.5

active: bool = True


# General pattern:
#
# variable: type = value


# ============================================================
# 2. FUNCTION PARAMETERS
# ============================================================

def greet(name: str):
    print(f"Hello {name}")


# name: str means:
#
# name is expected to be a string.


# ============================================================
# 3. RETURN TYPE
# ============================================================

def add(a: int, b: int) -> int:
    return a + b


# Read this as:
#
# add takes two integers and returns an integer.


def greet_user(name: str) -> str:
    return f"Hello {name}"


# -> str means:
#
# The function is expected to return a string.


# ============================================================
# 4. IMPORTANT: TYPE HINTS DO NOT ENFORCE TYPES
# ============================================================

def add_text(a: int, b: int) -> int:
    return a + b


# Python itself does NOT automatically stop this:

result = add_text("Hello", "World")

print(result)

# The result will be:
#
# HelloWorld
#
# Even though we said a and b should be int.
#
# Type hints are mainly used by:
#   - IDEs
#   - Linters
#   - Static type checkers
#   - Developers


# ============================================================
# 5. WHY TYPE HINTS ARE USEFUL FOR AI / API DEVELOPMENT
# ============================================================

def predict(age: int, bmi: float, smoker: bool) -> str:
    """
    Example of a function that could be part of an AI/API project.

    age    -> integer
    bmi    -> decimal number
    smoker -> True/False
    result -> string
    """

    return "Prediction result"


# Someone reading the function immediately knows:
#
# age    -> int
# bmi    -> float
# smoker -> bool
# result -> str


# ============================================================
# QUICK REFERENCE
# ============================================================

# Integer
number: int = 10

# String
text: str = "Hello"

# Decimal number
decimal: float = 10.5

# True / False
is_active: bool = True


# Function parameter types
def multiply(a: int, b: int):
    return a * b


# Function parameter + return type
def multiply_numbers(a: int, b: int) -> int:
    return a * b


# String function
def make_greeting(name: str) -> str:
    return f"Hello {name}"


# ============================================================
# SUMMARY
# ============================================================
#
# Variable:
#     age: int = 25
#
# Parameter:
#     def greet(name: str):
#
# Return type:
#     def add(a: int, b: int) -> int:
#
# Type hints:
#     - Make code easier to understand
#     - Help IDEs provide better suggestions
#     - Help static type checkers find mistakes
#     - Are especially useful in large projects and APIs
#
# IMPORTANT:
#     Type hints do not automatically enforce types at runtime.
# ============================================================