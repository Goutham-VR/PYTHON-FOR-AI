# ============================================================
# TYPE HINTS IN PYTHON
# PART 3: DICTIONARY TYPE HINTS
# ============================================================


# ============================================================
# 1. BASIC DICTIONARY TYPE HINT
# ============================================================

marks: dict[str, int] = {
    "Math": 90,
    "English": 85,
    "Science": 95
}


# dict[str, int] means:
#
# dict[
#     key type,
#     value type
# ]
#
# Here:
#
# key   -> str
# value -> int
#
# Therefore:
#
# "Math"    -> str
# 90        -> int
#
# "English" -> str
# 85        -> int
#
# "Science" -> str
# 95        -> int


# ============================================================
# 2. DICTIONARY WITH STRING VALUES
# ============================================================

student: dict[str, str] = {
    "name": "Alice",
    "city": "London",
    "course": "Python"
}


# Here:
#
# All keys are strings.
# All values are also strings.
#
# Therefore:
#
# dict[str, str]


# ============================================================
# 3. DICTIONARY WITH INTEGER VALUES
# ============================================================

marks: dict[str, int] = {
    "Math": 90,
    "English": 85,
    "Science": 95
}


# Here:
#
# Keys:
#
# "Math"
# "English"
# "Science"
#
# All are str.
#
# Values:
#
# 90
# 85
# 95
#
# All are int.
#
# Therefore:
#
# dict[str, int]


# ============================================================
# 4. DICTIONARY WITH DIFFERENT VALUE TYPES
# ============================================================

student: dict[str, str | int] = {
    "name": "Alice",
    "age": 20
}


# Here we have:
#
# "name" -> string
# "age"  -> string key
#
# Values:
#
# "Alice" -> str
# 20      -> int
#
# So the value can be:
#
# str OR int
#
# Therefore:
#
# dict[str, str | int]


# ============================================================
# 5. UNDERSTANDING dict[str, str | int]
# ============================================================

student: dict[str, str | int] = {
    "name": "Alice",
    "age": 20
}


# Read this as:
#
# dict[
#     key type,
#     value type
# ]
#
#
# dict[
#     str,
#     str | int
# ]
#
#
# Key:
#
# str
#
# Value:
#
# str OR int


# The | symbol means OR.
#
# Therefore:
#
# str | int
#
# means:
#
# string OR integer.


# ============================================================
# 6. WHY dict[str, str] IS WRONG HERE
# ============================================================

student = {
    "name": "Alice",
    "age": 20
}


# If we write:
#
# student: dict[str, str]
#
# We are saying:
#
#     All keys -> str
#     All values -> str
#
# But:
#
# "Alice" -> str
# 20      -> int
#
# The value 20 is not a string.
#
# Therefore:
#
# dict[str, str]
#
# does not correctly describe this dictionary.


# Correct:
#
# dict[str, str | int]


# ============================================================
# 7. DICTIONARY FUNCTION PARAMETER
# ============================================================

def print_marks(marks: dict[str, int]) -> None:
    for subject, mark in marks.items():
        print(subject, mark)


# Here:
#
# marks -> dictionary
#
# key:
#     str
#
# value:
#     int
#
# return:
#     None


# Example:

marks: dict[str, int] = {
    "Math": 90,
    "English": 85,
    "Science": 95
}

print_marks(marks)


# Output:
#
# Math 90
# English 85
# Science 95


# ============================================================
# 8. DICTIONARY .items()
# ============================================================

marks: dict[str, int] = {
    "Math": 90,
    "English": 85,
    "Science": 95
}

for subject, mark in marks.items():
    print(subject, mark)


# .items() gives us:
#
# key + value
#
#
# First iteration:
#
# subject = "Math"
# mark = 90
#
#
# Second iteration:
#
# subject = "English"
# mark = 85
#
#
# Third iteration:
#
# subject = "Science"
# mark = 95


# ============================================================
# 9. DICTIONARY WITH LIST VALUES
# ============================================================

students: dict[str, list[int]] = {
    "Alice": [90, 85, 95],
    "John": [80, 75, 88]
}


# Here:
#
# Keys:
#
# "Alice"
# "John"
#
# Both are str.
#
# Values:
#
# [90, 85, 95]
# [80, 75, 88]
#
# Both are list[int].
#
# Therefore:
#
# dict[str, list[int]]


# Read it as:
#
# dictionary
#     key   -> str
#     value -> list[int]


# ============================================================
# 10. DICTIONARY WITH LIST OF STRINGS
# ============================================================

subjects: dict[str, list[str]] = {
    "Alice": ["Math", "English"],
    "John": ["Science", "Physics"]
}


# Key:
#
# str
#
# Value:
#
# list[str]
#
# Therefore:
#
# dict[str, list[str]]


# ============================================================
# 11. FUNCTION RETURNING A DICTIONARY
# ============================================================

def get_marks() -> dict[str, int]:
    return {
        "Math": 90,
        "English": 85,
        "Science": 95
    }


# Read this as:
#
# get_marks()
#
# returns:
#
# dict[str, int]


# The function returns a dictionary where:
#
# keys   -> str
# values -> int


# ============================================================
# 12. DICTIONARY TYPE HINT QUICK REFERENCE
# ============================================================

# Dictionary with string keys and string values:

dict[str, str]


# Dictionary with string keys and integer values:

dict[str, int]


# Dictionary with integer keys and string values:

dict[int, str]


# Dictionary with string keys and float values:

dict[str, float]


# Dictionary with string keys and boolean values:

dict[str, bool]


# Dictionary with string keys and list of integers:

dict[str, list[int]]


# Dictionary with string keys and multiple possible value types:

dict[str, str | int]


# ============================================================
# 13. OLD STYLE USING typing.Dict
# ============================================================

from typing import Dict


student: Dict[str, int] = {
    "age": 20
}


# This was commonly used in older Python code.
#
# Modern Python can simply use:
#
# dict[str, int]
#
# which is cleaner.


# ============================================================
# 14. OLD STYLE USING Union
# ============================================================

from typing import Union


student: dict[str, Union[str, int]] = {
    "name": "Alice",
    "age": 20
}


# Modern Python:
#
# dict[str, str | int]
#
# is equivalent and cleaner.


# ============================================================
# 15. IMPORTANT: TYPE HINTS DO NOT ENFORCE TYPES
# ============================================================

marks: dict[str, int] = {
    "Math": 90,
    "English": 85
}


# Type hints tell us what we EXPECT.
#
# They are mainly useful for:
#
#     - IDEs
#     - Linters
#     - Static type checkers
#     - Developers
#
# Python does not automatically enforce the type hint
# at runtime.


# ============================================================
# 16. QUICK SUMMARY
# ============================================================

# Dictionary syntax:
#
# dict[key_type, value_type]


# Example:

marks: dict[str, int] = {
    "Math": 90,
    "English": 85
}


# Means:
#
# keys   -> str
# values -> int


# Multiple possible value types:

student: dict[str, str | int] = {
    "name": "Alice",
    "age": 20
}


# Means:
#
# keys   -> str
# values -> str OR int


# Dictionary containing lists:

students: dict[str, list[int]] = {
    "Alice": [90, 85, 95]
}


# Means:
#
# keys   -> str
# values -> list[int]


# ============================================================
# KEY IDEA
# ============================================================
#
# dict[key_type, value_type]
#
# tells us:
#
#     What type are the keys?
#     What type are the values?
#
#
# Examples:
#
# dict[str, int]
#     -> string keys
#        integer values
#
#
# dict[str, str]
#     -> string keys
#        string values
#
#
# dict[str, str | int]
#     -> string keys
#        string OR integer values
#
#
# dict[str, list[int]]
#     -> string keys
#        list of integers as values
#
#
# Remember:
#
# The first type describes the KEY.
# The second type describes the VALUE.
#
# ============================================================