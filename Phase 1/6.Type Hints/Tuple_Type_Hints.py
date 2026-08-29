# ============================================================
# TYPE HINTS IN PYTHON
# PART 4: TUPLE TYPE HINTS
# ============================================================


# ============================================================
# 1. BASIC TUPLE TYPE HINT
# ============================================================

point: tuple[int, int] = (10, 20)


# tuple[int, int] means:
#
# Position 1 -> int
# Position 2 -> int
#
#
# Therefore:
#
# 10 -> int
# 20 -> int


# ============================================================
# 2. TUPLE WITH DIFFERENT TYPES
# ============================================================

student: tuple[str, int] = ("Alice", 20)


# Here:
#
# Position 1:
#
# "Alice" -> str
#
#
# Position 2:
#
# 20 -> int
#
#
# Therefore:
#
# tuple[str, int]


# ============================================================
# 3. THREE DIFFERENT TYPES
# ============================================================

data: tuple[str, int, float] = ("Alice", 20, 85.5)


# Read it as:
#
# tuple[
#     position 1 type,
#     position 2 type,
#     position 3 type
# ]
#
#
# Position 1 -> str   -> "Alice"
# Position 2 -> int   -> 20
# Position 3 -> float -> 85.5


# ============================================================
# 4. TUPLE POSITION MATTERS
# ============================================================

data: tuple[str, int] = ("Alice", 20)


# This is correct because:
#
# Position 1 -> str
# Position 2 -> int


# But:

data: tuple[str, int] = (20, "Alice")


# This does NOT match the expected tuple type.
#
# Why?
#
# Position 1 expects:
#
# str
#
# But received:
#
# int
#
#
# Position 2 expects:
#
# int
#
# But received:
#
# str


# ============================================================
# 5. TUPLE VS LIST
# ============================================================

numbers: list[int] = [10, 20, 30]


# list[int] means:
#
# The list contains integers.
#
# Example:
#
# [10, 20, 30]


# A tuple can describe each position:

data: tuple[str, int, float] = ("Alice", 20, 85.5)


# Meaning:
#
# Position 1 -> str
# Position 2 -> int
# Position 3 -> float


# ============================================================
# 6. FIXED-LENGTH TUPLE
# ============================================================

person: tuple[str, int, str] = (
    "Alice",
    20,
    "Developer"
)


# This describes exactly three positions:
#
# Position 1 -> str
# Position 2 -> int
# Position 3 -> str
#
#
# So the expected structure is:
#
# (string, integer, string)


# Example:
#
# ("Alice", 20, "Developer")
#       ↓      ↓       ↓
#      str    int     str


# ============================================================
# 7. VARIABLE-LENGTH TUPLE
# ============================================================

numbers: tuple[int, ...] = (10, 20, 30, 40, 50)


# Notice:
#
# tuple[int, ...]
#
# The ... means:
#
# Any number of elements,
# but every element must be an int.


# Therefore these are valid:

numbers: tuple[int, ...] = (10,)

numbers: tuple[int, ...] = (10, 20)

numbers: tuple[int, ...] = (10, 20, 30, 40)


# All elements are integers.


# ============================================================
# 8. WHY DO WE USE ...?
# ============================================================

numbers: tuple[int, ...] = (10, 20, 30)


# Read this as:
#
# tuple[
#     int,
#     ...
# ]
#
#
# Meaning:
#
# One or more integers can appear in the tuple.
#
# The number of elements is not fixed.


# Compare:


point: tuple[int, int] = (10, 20)


# Exactly:
#
# 2 elements
#
#
# Whereas:


numbers: tuple[int, ...] = (10, 20, 30, 40)


# Can contain:
#
# 1 element
# 2 elements
# 3 elements
# 4 elements
# ...
#
# As long as every element is an int.


# ============================================================
# 9. VARIABLE-LENGTH STRING TUPLE
# ============================================================

names: tuple[str, ...] = (
    "Alice",
    "John",
    "Bob"
)


# Means:
#
# Any number of elements
# but every element must be a string.


# Examples:

names: tuple[str, ...] = ("Alice",)

names: tuple[str, ...] = ("Alice", "John")

names: tuple[str, ...] = ("Alice", "John", "Bob")


# All are valid structures.


# ============================================================
# 10. MIXED TYPES WITH FIXED POSITIONS
# ============================================================

employee: tuple[str, int, float] = (
    "Alice",
    25,
    45000.50
)


# Meaning:
#
# Position 1 -> str
# Position 2 -> int
# Position 3 -> float
#
#
# Therefore:
#
# "Alice"    -> str
# 25         -> int
# 45000.50   -> float


# ============================================================
# 11. TUPLE AS A FUNCTION PARAMETER
# ============================================================

def display_point(point: tuple[int, int]) -> None:
    print("X:", point[0])
    print("Y:", point[1])


# The parameter:
#
# point -> tuple[int, int]
#
# means:
#
# point must contain:
#
# Position 1 -> int
# Position 2 -> int


# Example:

point: tuple[int, int] = (10, 20)

display_point(point)


# Output:
#
# X: 10
# Y: 20


# ============================================================
# 12. FUNCTION RETURNING A TUPLE
# ============================================================

def get_point() -> tuple[int, int]:
    return (10, 20)


# Read this as:
#
# get_point()
#
# returns:
#
# tuple[int, int]
#
#
# Meaning:
#
# The function returns a tuple containing:
#
# int at position 1
# int at position 2


# ============================================================
# 13. TUPLE UNPACKING
# ============================================================

student: tuple[str, int] = ("Alice", 20)

name, age = student


# After unpacking:
#
# name -> "Alice"
# age  -> 20


# The tuple:
#
# ("Alice", 20)
#
# becomes:
#
# name = "Alice"
# age  = 20


# ============================================================
# 14. TUPLE WITH BOOLEAN VALUES
# ============================================================

status: tuple[str, bool] = (
    "Login",
    True
)


# Position 1:
#
# "Login" -> str
#
#
# Position 2:
#
# True -> bool
#
#
# Therefore:
#
# tuple[str, bool]


# ============================================================
# 15. TUPLE WITH A LIST
# ============================================================

student: tuple[str, list[int]] = (
    "Alice",
    [90, 85, 95]
)


# Position 1:
#
# "Alice" -> str
#
#
# Position 2:
#
# [90, 85, 95] -> list[int]
#
#
# Therefore:
#
# tuple[str, list[int]]


# ============================================================
# 16. QUICK REFERENCE
# ============================================================

# Two integers:

tuple[int, int]


# String followed by integer:

tuple[str, int]


# String, integer and float:

tuple[str, int, float]


# Any number of integers:

tuple[int, ...]


# Any number of strings:

tuple[str, ...]


# String followed by boolean:

tuple[str, bool]


# String followed by list of integers:

tuple[str, list[int]]


# ============================================================
# 17. FIXED LENGTH VS VARIABLE LENGTH
# ============================================================

# FIXED LENGTH
#
# tuple[int, int]
#
# Exactly 2 integers.


point: tuple[int, int] = (10, 20)


# VARIABLE LENGTH
#
# tuple[int, ...]
#
# Any number of integers.


numbers: tuple[int, ...] = (10, 20, 30, 40)


# Remember:
#
# tuple[int, int]
#       ↑    ↑
#       position-specific types
#
#
# tuple[int, ...]
#       ↑     ↑
#       type  any number of elements


# ============================================================
# 18. IMPORTANT DIFFERENCE
# ============================================================

# list[int]
#
# A list containing integers.


numbers: list[int] = [10, 20, 30]


# tuple[int, int, int]
#
# A tuple with exactly 3 integer positions.


numbers: tuple[int, int, int] = (10, 20, 30)


# tuple[int, ...]
#
# A tuple containing any number of integers.


numbers: tuple[int, ...] = (10, 20, 30, 40, 50)


# ============================================================
# 19. QUICK SUMMARY
# ============================================================

# tuple[int, int]
#     -> exactly 2 integers
#
#
# tuple[str, int]
#     -> position 1 is str
#        position 2 is int
#
#
# tuple[str, int, float]
#     -> position 1 is str
#        position 2 is int
#        position 3 is float
#
#
# tuple[int, ...]
#     -> any number of integers
#
#
# tuple[str, ...]
#     -> any number of strings


# ============================================================
# KEY IDEA
# ============================================================
#
# Tuple type hints can describe the type of EACH POSITION.
#
#
# Example:
#
# tuple[str, int, float]
#
# means:
#
# Position 1 -> str
# Position 2 -> int
# Position 3 -> float
#
#
# The ... has a special meaning:
#
# tuple[int, ...]
#
# means:
#
# Any number of elements,
# but every element must be an int.
#
#
# So remember:
#
# tuple[int, int]
#     -> fixed positions
#
# tuple[int, ...]
#     -> variable number of elements
#
# ============================================================