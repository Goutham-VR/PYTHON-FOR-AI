# ============================================================
# TYPE HINTS IN PYTHON
# PART 7: ANY TYPE HINT
# ============================================================


# ============================================================
# 1. WHAT IS Any?
# ============================================================

from typing import Any


data: Any


# Any means:
#
# data can contain any type of value.
#
#
# For example:
#
# int
# str
# float
# bool
# list
# dict
# tuple
# object
# etc.


# ============================================================
# 2. ANY CAN HOLD DIFFERENT TYPES
# ============================================================

data: Any = 10


# int


data = "Hello"


# str


data = [1, 2, 3]


# list


data = {
    "name": "Alice"
}


# dict


data = (10, 20)


# tuple


# All of these are allowed with:
#
# data: Any


# ============================================================
# 3. COMPARE Any WITH int
# ============================================================

data: int = 10


# Here:
#
# data is expected to contain an int.
#
#
# Example:

data = 100


# Correct.


# But:

data = "Hello"


# This does not match the expected type.
#
# Why?
#
# Expected:
#
# int
#
# Received:
#
# str


# ============================================================
# 4. COMPARE Any WITH UNION
# ============================================================

data: int | str


# This means:
#
# data can be:
#
# int
# OR
# str


data = 100


# Valid.


data = "Hello"


# Also valid.


data = 10.5


# Not expected because:
#
# float is not included.


# ============================================================
# 5. Any MEANS ANYTHING
# ============================================================

data: Any


# This allows:

data = 10

data = "Hello"

data = 10.5

data = True

data = [1, 2, 3]

data = {
    "name": "Alice"
}

data = (10, 20)


# All are allowed by the type hint.


# ============================================================
# 6. SPECIFIC TYPE VS UNION VS Any
# ============================================================

# Most specific:

data: int


# Only int is expected.


# Less specific:

data: int | str


# int OR str is expected.


# Least specific:

data: Any


# Any type is allowed.


# Think of it as:
#
#
# int
#  ↓
# int | str
#  ↓
# Any
#
#
# As more possibilities are allowed,
# the type hint becomes less specific.


# ============================================================
# 7. MOST SPECIFIC TYPE
# ============================================================

# Example:

age: int


# This gives very precise information:
#
# age should be an integer.


# Compared with:

age: int | float


# Now age can be:
#
# int
# OR
# float


# Compared with:

age: Any


# Now age can be anything.


# Therefore:
#
# int
#     -> most specific
#
# int | float
#     -> less specific
#
# Any
#     -> least specific


# ============================================================
# 8. Any IN A FUNCTION
# ============================================================

def process(data: Any) -> Any:
    return data


# The parameter:
#
# data: Any
#
# means:
#
# the function accepts any type.
#
#
# The return type:
#
# -> Any
#
# means:
#
# the function may return any type.


process(100)

process("Hello")

process([1, 2, 3])

process({
    "name": "Alice"
})


# All are allowed.


# ============================================================
# 9. Any AS A FUNCTION PARAMETER
# ============================================================

def display(data: Any) -> None:
    print(data)


# The function can receive any type.


display(100)

display("Hello")

display([10, 20])

display({
    "name": "Alice"
})


# ============================================================
# 10. Any WITH LIST
# ============================================================

values: list[Any] = [
    10,
    "Hello",
    10.5,
    True
]


# This means:
#
# values is a list.
#
# Each element can be any type.


# Compare:


numbers: list[int] = [
    10,
    20,
    30
]


# Here every element is expected to be int.


# Whereas:

values: list[Any] = [
    10,
    "Hello",
    10.5
]


# Different types are allowed.


# ============================================================
# 11. Any WITH DICTIONARY
# ============================================================

data: dict[str, Any] = {
    "name": "Alice",
    "age": 20,
    "height": 5.6,
    "active": True
}


# Here:
#
# Keys:
#     str
#
# Values:
#     Any
#
#
# Therefore:
#
# dict[str, Any]


# Different value types are allowed:
#
# "Alice" -> str
# 20      -> int
# 5.6     -> float
# True    -> bool


# ============================================================
# 12. Any WITH API DATA
# ============================================================

# data: Any = get_api_response()


# Imagine an API returns data
# whose structure is not known in advance.
#
# Any can be useful in this situation.


# Example:

data: Any = {
    "name": "Alice",
    "age": 20
}


# The API could potentially return
# a different structure.


# ============================================================
# 13. Any WITH JSON DATA
# ============================================================

json_data: Any = {
    "name": "Alice",
    "age": 20,
    "skills": [
        "Python",
        "Django"
    ]
}


# JSON data can contain different types:
#
# string
# integer
# float
# boolean
# list
# dictionary
# null
#
#
# Therefore Any can sometimes be useful
# when the exact structure is unknown.


# ============================================================
# 14. Any IS NOT THE SAME AS object
# ============================================================

from typing import Any


data: Any


data: object


# These are NOT exactly the same concept.
#
#
# Any tells the type checker:
#
# "Don't restrict this value based on its type."
#
#
# object means:
#
# "This value is some Python object."
#
#
# Any provides much less type-checking information.


# ============================================================
# 15. WHY NOT USE Any EVERYWHERE?
# ============================================================

# Imagine:

def calculate(age: Any) -> Any:
    ...


# We now don't know:
#
# What type should age be?
#
# What type does the function return?
#
#
# This makes the code harder to understand.


# Better:

def calculate(age: int) -> int:
    ...


# Now we know:
#
# age -> int
#
# return -> int


# ============================================================
# 16. SPECIFIC TYPES ARE BETTER WHEN KNOWN
# ============================================================

# Bad choice when we know the type:

name: Any = "Alice"


# Better:

name: str = "Alice"


# Bad:

age: Any = 25


# Better:

age: int = 25


# Bad:

marks: Any = [90, 85, 95]


# Better:

marks: list[int] = [90, 85, 95]


# Use the most specific type
# that accurately describes your data.


# ============================================================
# 17. Any VS UNION
# ============================================================

# Suppose a value can only be:
#
# int
# OR
# str


value: int | str


# This is better than:

value: Any


# Why?
#
# int | str gives the type checker
# useful information.
#
#
# Any says:
#
# "It could be anything."


# Therefore, if you know the possible types,
# use a Union instead of Any.


# ============================================================
# 18. REAL APPLICATION EXAMPLE
# ============================================================

def process_user_id(user_id: int) -> str:
    return str(user_id)


# We know exactly what user_id should be:
#
# int


# So:

user_id: int


# is better than:

user_id: Any


# ============================================================
# 19. WHEN Any CAN BE USEFUL
# ============================================================

# Any can be useful when:
#
#     - The type genuinely cannot be known.
#     - Data comes from a dynamic external source.
#     - Working with loosely structured JSON.
#     - Integrating with poorly typed libraries.
#     - Building intentionally flexible interfaces.
#
#
# But it should not be the default choice.


# ============================================================
# 20. QUICK COMPARISON
# ============================================================

# Specific type:

data: int


# Meaning:
#
# integer only.


# Union:

data: int | str


# Meaning:
#
# integer OR string.


# Any:

data: Any


# Meaning:
#
# any type.


# ============================================================
# 21. SPECIFICITY ORDER
# ============================================================

# Most specific:

data: int


# Then:

data: int | str


# Then:

data: Any


# Think:

#
#       MORE SPECIFIC
#             ↑
#             |
#            int
#             |
#        int | str
#             |
#            Any
#             |
#             ↓
#       LESS SPECIFIC
#


# ============================================================
# 22. QUICK REFERENCE
# ============================================================

# Integer:

int


# String:

str


# Integer OR string:

int | str


# Integer OR float OR string:

int | float | str


# Anything:

Any


# List containing anything:

list[Any]


# Dictionary with string keys
# and any type of values:

dict[str, Any]


# ============================================================
# 23. QUICK SUMMARY
# ============================================================

from typing import Any


data: Any


# Means:
#
# data can contain any type.


# Compare:


data: int


# -> integer only


data: int | str


# -> integer OR string


data: Any


# -> any type


# Therefore:
#
# int
#     -> most specific
#
# int | str
#     -> less specific
#
# Any
#     -> least specific


# ============================================================
# KEY IDEA
# ============================================================
#
# Any means:
#
#     "This value can be any type."
#
#
# It is useful when the type genuinely cannot be determined
# or is intentionally flexible.
#
#
# But:
#
# If you know the type:
#
#     name: str
#
# use it.
#
#
# If you know the possible types:
#
#     value: int | str
#
# use a Union.
#
#
# Use:
#
#     Any
#
# only when you genuinely need that flexibility.
#
#
# Remember:
#
# int
#     -> integer
#
# int | str
#     -> integer OR string
#
# Any
#     -> anything
#
# ============================================================