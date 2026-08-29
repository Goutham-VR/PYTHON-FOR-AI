# ============================================================
# TYPE HINTS IN PYTHON
# PART 10: TYPEVAR
# ============================================================


# ============================================================
# 1. THE PROBLEM: SAME FUNCTION, DIFFERENT TYPES
# ============================================================

# Suppose we have a function that gets
# the first item from a list.


def first(numbers: list[int]) -> int:
    return numbers[0]


# This function works with integers:

result = first([10, 20, 30])

print(result)


# Output:
#
# 10


# Its type relationship is:
#
# Input:
#     list[int]
#
# Output:
#     int


# ============================================================
# 2. THE SAME LOGIC WITH STRINGS
# ============================================================

def first_string(names: list[str]) -> str:
    return names[0]


result = first_string(
    ["Alice", "Bob", "John"]
)

print(result)


# Output:
#
# Alice


# Its type relationship is:
#
# Input:
#     list[str]
#
# Output:
#     str


# ============================================================
# 3. THE PROBLEM
# ============================================================

# The logic of both functions is exactly the same:
#
#     return items[0]
#
#
# The only difference is the type.


def first_int(numbers: list[int]) -> int:
    return numbers[0]


def first_string(names: list[str]) -> str:
    return names[0]


# We don't really want to duplicate
# the same logic.


# We want ONE function that works with:
#
# list[int]
# list[str]
# list[float]
# etc.


# ============================================================
# 4. TYPEVAR
# ============================================================

from typing import TypeVar


T = TypeVar("T")


# T is a type variable.
#
# Think of T as:
#
#     a placeholder for a type.
#
#
# We don't decide what T is yet.


# ============================================================
# 5. USING T IN A FUNCTION
# ============================================================

def first(items: list[T]) -> T:
    return items[0]


# Read this slowly:
#
#
# items: list[T]
#
# means:
#
# items is a list containing values of type T.
#
#
# -> T
#
# means:
#
# the function returns a value of type T.


# In simple words:
#
# Whatever type goes into the list,
# the same type comes out.


# ============================================================
# 6. T = int
# ============================================================

numbers = [10, 20, 30]


result = first(numbers)


# Python sees:
#
# numbers -> list[int]
#
#
# Therefore:
#
# T = int
#
#
# Conceptually, the function becomes:
#
# def first(items: list[int]) -> int:
#     return items[0]


print(result)


# Output:
#
# 10


# Therefore:
#
# T = int
#
# result -> int
# result = 10


# ============================================================
# 7. T = str
# ============================================================

names = [
    "Alice",
    "Bob",
    "John"
]


result = first(names)


# Python sees:
#
# names -> list[str]
#
#
# Therefore:
#
# T = str
#
#
# Conceptually:
#
# def first(items: list[str]) -> str:
#     return items[0]


print(result)


# Output:
#
# Alice


# Therefore:
#
# T = str
#
# result -> str
# result = "Alice"


# ============================================================
# 8. T = float
# ============================================================

prices = [
    10.5,
    20.75,
    30.99
]


result = first(prices)


# Python sees:
#
# prices -> list[float]
#
#
# Therefore:
#
# T = float
#
#
# Conceptually:
#
# def first(items: list[float]) -> float:
#     return items[0]


print(result)


# Output:
#
# 10.5


# Therefore:
#
# T = float
#
# result -> float


# ============================================================
# 9. THE MAIN IDEA
# ============================================================

T


# Think of T as:
#
#     "Whatever type comes in."


# Example:
#
#
# list[int]
#     ↓
# T = int
#     ↓
# int
#
#
# list[str]
#     ↓
# T = str
#     ↓
# str
#
#
# list[float]
#     ↓
# T = float
#     ↓
# float


# ============================================================
# 10. TYPE RELATIONSHIP
# ============================================================

def first(items: list[T]) -> T:
    return items[0]


# The important relationship is:
#
#
# Input:
#
# list[T]
#
#       ↓
#
#       T
#
#       ↓
#
# Output:
#
# T
#
#
# The same T is used for both input and output.


# ============================================================
# 11. WHY NOT USE Any?
# ============================================================

# We could write:

from typing import Any


def first(items: list[Any]) -> Any:
    return items[0]


# This technically allows many types.
#
# But there is an important difference.


# Any means:
#
# "I don't know or don't care about the type."


# TypeVar means:
#
# "The input and output types are related."


# With TypeVar:

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


# If:
#
# list[int]
#
# goes in:
#
# int
#
# comes out.
#
#
# If:
#
# list[str]
#
# goes in:
#
# str
#
# comes out.


# ============================================================
# 12. TypeVar PRESERVES THE TYPE
# ============================================================

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


numbers = [10, 20, 30]

number = first(numbers)


# Type:
#
# number -> int


names = ["Alice", "Bob"]

name = first(names)


# Type:
#
# name -> str


# The type of the result is connected
# to the type of the input.


# ============================================================
# 13. ANOTHER EXAMPLE: GET LAST ITEM
# ============================================================

T = TypeVar("T")


def last(items: list[T]) -> T:
    return items[-1]


numbers = [10, 20, 30]

result = last(numbers)


# T = int
#
# result -> int
#
# result = 30


names = ["Alice", "Bob", "John"]

result = last(names)


# T = str
#
# result -> str
#
# result = "John"


# ============================================================
# 14. SWAP TWO VALUES
# ============================================================

T = TypeVar("T")


def repeat(value: T) -> tuple[T, T]:
    return value, value


# If:

result = repeat(10)


# Then:
#
# T = int
#
# result:
#
# tuple[int, int]


# If:

result = repeat("Hello")


# Then:
#
# T = str
#
# result:
#
# tuple[str, str]


# ============================================================
# 15. TYPEVAR WITH A FUNCTION
# ============================================================

T = TypeVar("T")


def identity(value: T) -> T:
    return value


# This function simply returns
# whatever value it receives.


result = identity(100)


# T = int
#
# result -> int


result = identity("Hello")


# T = str
#
# result -> str


result = identity(10.5)


# T = float
#
# result -> float


# ============================================================
# 16. IDENTITY FUNCTION
# ============================================================

def identity(value: T) -> T:
    return value


# This is a classic example of TypeVar.
#
#
# Input:
#     T
#
# Output:
#     T
#
#
# Whatever type enters,
# the same type comes out.


# ============================================================
# 17. TYPEVAR WITH TUPLE
# ============================================================

T = TypeVar("T")


def make_pair(value: T) -> tuple[T, T]:
    return (value, value)


result = make_pair(10)


# T = int
#
# result -> tuple[int, int]


result = make_pair("Alice")


# T = str
#
# result -> tuple[str, str]


# ============================================================
# 18. TYPEVAR WITH DICTIONARY VALUES
# ============================================================

T = TypeVar("T")


def get_value(
    data: dict[str, T],
    key: str
) -> T:

    return data[key]


marks: dict[str, int] = {
    "Math": 90,
    "English": 85
}


result = get_value(
    marks,
    "Math"
)


# T = int
#
# result -> int
#
# result = 90


# Another dictionary:

names: dict[str, str] = {
    "student1": "Alice",
    "student2": "John"
}


result = get_value(
    names,
    "student1"
)


# T = str
#
# result -> str
#
# result = "Alice"


# ============================================================
# 19. TYPEVAR WITH LISTS
# ============================================================

T = TypeVar("T")


def get_first(items: list[T]) -> T:
    return items[0]


# Integer list:

numbers: list[int] = [10, 20, 30]

number = get_first(numbers)


# T = int


# String list:

names: list[str] = [
    "Alice",
    "Bob"
]

name = get_first(names)


# T = str


# Float list:

prices: list[float] = [
    10.5,
    20.5
]

price = get_first(prices)


# T = float


# ============================================================
# 20. TYPEVAR WITH MULTIPLE PARAMETERS
# ============================================================

T = TypeVar("T")


def same_value(
    first: T,
    second: T
) -> T:

    return first


# Both parameters are expected
# to use the same type T.


same_value(10, 20)


# T = int


same_value(
    "Alice",
    "Bob"
)


# T = str


# Conceptually:
#
# same_value(10, 20)
#
# becomes:
#
# same_value(int, int) -> int
#
#
# same_value("Alice", "Bob")
#
# becomes:
#
# same_value(str, str) -> str


# ============================================================
# 21. TYPE SAFETY WITH TypeVar
# ============================================================

T = TypeVar("T")


def same_value(
    first: T,
    second: T
) -> T:

    return first


# The two parameters are connected
# through the same T.


# This is good:

same_value(10, 20)


# Both:
#
# int
# int


# This is also good:

same_value(
    "Alice",
    "Bob"
)


# Both:
#
# str
# str


# Mixing unrelated types may not match
# the intended relationship:

same_value(
    10,
    "Alice"
)


# The type checker can warn about
# the inconsistent types.


# ============================================================
# 22. TypeVar VS UNION
# ============================================================

# UNION:

def process(value: int | str) -> int | str:
    return value


# This means:
#
# input can be int OR str
#
# output can be int OR str
#
#
# But it does not express
# the relationship between them.


# TYPEVAR:

T = TypeVar("T")


def identity(value: T) -> T:
    return value


# This means:
#
# input type and output type
# are the SAME type.


# Example:
#
# int -> int
#
# str -> str
#
# float -> float


# ============================================================
# 23. TypeVar VS Any
# ============================================================

# Any:

def identity(value: Any) -> Any:
    return value


# Any gives very little information
# to the type checker.


# TypeVar:

T = TypeVar("T")


def identity(value: T) -> T:
    return value


# TypeVar tells the type checker:
#
# "The output type depends on
# the input type."


# ============================================================
# 24. GENERIC THINKING
# ============================================================

# TypeVar is the foundation of
# generic programming in Python.
#
#
# Instead of writing:

def first_int(items: list[int]) -> int:
    return items[0]


def first_str(items: list[str]) -> str:
    return items[0]


def first_float(items: list[float]) -> float:
    return items[0]


# We can write one generic function:

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


# One function can represent
# all those cases.


# ============================================================
# 25. QUICK REFERENCE
# ============================================================

from typing import TypeVar


T = TypeVar("T")


# Generic value:

def identity(value: T) -> T:
    return value


# Generic list:

def first(items: list[T]) -> T:
    return items[0]


# Generic tuple:

def make_pair(value: T) -> tuple[T, T]:
    return (value, value)


# Generic dictionary:

def get_value(
    data: dict[str, T],
    key: str
) -> T:

    return data[key]


# ============================================================
# 26. THE MOST IMPORTANT EXAMPLE
# ============================================================

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


numbers = [10, 20, 30]

result = first(numbers)


# Input:
#
# list[int]
#
# Therefore:
#
# T = int
#
# Output:
#
# int
#
# result = 10


names = [
    "Alice",
    "Bob",
    "John"
]

result = first(names)


# Input:
#
# list[str]
#
# Therefore:
#
# T = str
#
# Output:
#
# str
#
# result = "Alice"


# ============================================================
# 27. QUICK SUMMARY
# ============================================================

# Create a TypeVar:

T = TypeVar("T")


# Use it in a function:

def first(items: list[T]) -> T:
    return items[0]


# Integer input:

first([10, 20, 30])


# T = int
#
# result -> int


# String input:

first(["Alice", "Bob"])


# T = str
#
# result -> str


# Float input:

first([10.5, 20.5])


# T = float
#
# result -> float


# ============================================================
# KEY IDEA
# ============================================================
#
# TypeVar creates a placeholder for a type.
#
#
# T = TypeVar("T")
#
#
# Think of T as:
#
#     "Whatever type comes in."
#
#
# Example:
#
# def first(items: list[T]) -> T:
#     return items[0]
#
#
# If input is:
#
# list[int]
#
# then:
#
# T = int
#
# and output:
#
# int
#
#
# If input is:
#
# list[str]
#
# then:
#
# T = str
#
# and output:
#
# str
#
#
# If input is:
#
# list[float]
#
# then:
#
# T = float
#
# and output:
#
# float
#
#
# The most important idea:
#
#                 T
#                 ↓
# Input ───────→  T  ───────→ Output
#
#
# The same T connects the input type
# with the output type.
#
#
# Remember:
#
# Any
#     -> anything
#
# Union
#     -> one of several allowed types
#
# TypeVar
#     -> a type placeholder that preserves
#        the relationship between types
#
# ============================================================