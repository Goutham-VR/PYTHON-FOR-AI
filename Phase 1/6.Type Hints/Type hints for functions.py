# ============================================================
# TYPE HINTS IN PYTHON
# PART 9: TYPE HINTS FOR FUNCTIONS
# ============================================================


# ============================================================
# 1. COMBINING EVERYTHING
# ============================================================

# We can combine different type hints
# inside a single function.
#
# Example:

from typing import Callable


def process(
    name: str,
    age: int,
    callback: Callable[[str], int]
) -> int:

    return callback(name)


# Let's break this function down.


# ============================================================
# 2. PARAMETER: name
# ============================================================

name: str


# This means:
#
# name should be a string.


# Example:

process(
    "Alice",
    20,
    ...
)


# "Alice" -> str


# ============================================================
# 3. PARAMETER: age
# ============================================================

age: int


# This means:
#
# age should be an integer.
#
#
# Example:
#
# 20 -> int


# ============================================================
# 4. PARAMETER: callback
# ============================================================

callback: Callable[[str], int]


# This is the most interesting parameter.
#
#
# Callable[[str], int]
#
# means:
#
# callback must be a function that:
#
#     accepts one str parameter
#     returns an int


# In simple form:
#
#
# callback
#     ↓
# function
#     ↓
# takes str
#     ↓
# returns int


# ============================================================
# 5. RETURN TYPE
# ============================================================

def process(
    name: str,
    age: int,
    callback: Callable[[str], int]
) -> int:


# The:
#
# -> int
#
# means:
#
# process() returns an integer.


# ============================================================
# 6. COMPLETE FUNCTION
# ============================================================

def process(
    name: str,
    age: int,
    callback: Callable[[str], int]
) -> int:

    return callback(name)


# The function has:
#
# name:
#     str
#
# age:
#     int
#
# callback:
#     Callable[[str], int]
#
# return:
#     int


# ============================================================
# 7. CREATING A CALLBACK
# ============================================================

def get_length(text: str) -> int:
    return len(text)


# Let's check its type:
#
# Input:
#     str
#
# Output:
#     int
#
#
# Therefore get_length matches:
#
# Callable[[str], int]


# ============================================================
# 8. PASSING THE FUNCTION
# ============================================================

result = process(
    "Alice",
    20,
    get_length
)


print(result)


# Output:
#
# 5


# Why?
#
# process() receives:
#
# name = "Alice"
# age = 20
# callback = get_length
#
#
# Then:
#
# return callback(name)
#
#
# becomes:
#
# return get_length("Alice")
#
#
# get_length("Alice")
#
# returns:
#
# 5


# ============================================================
# 9. IMPORTANT: age IS NOT USED HERE
# ============================================================

def process(
    name: str,
    age: int,
    callback: Callable[[str], int]
) -> int:

    return callback(name)


# Notice:
#
# age is accepted by the function,
# but it is not currently used.
#
# It is still type-hinted as:
#
# age: int


# ============================================================
# 10. ANOTHER CALLBACK
# ============================================================

def count_characters(text: str) -> int:
    return len(text)


result = process(
    "Hello World",
    25,
    count_characters
)


print(result)


# Output:
#
# 11


# count_characters matches:
#
# Callable[[str], int]


# ============================================================
# 11. ANOTHER CALLBACK
# ============================================================

def calculate_score(name: str) -> int:
    return len(name) * 10


result = process(
    "Alice",
    20,
    calculate_score
)


print(result)


# Output:
#
# 50


# Again:
#
# calculate_score:
#
# input:
#     str
#
# output:
#     int
#
#
# Therefore it matches:
#
# Callable[[str], int]


# ============================================================
# 12. WRONG CALLBACK
# ============================================================

def get_name(number: int) -> str:
    return str(number)


# This function has:
#
# input:
#     int
#
# output:
#     str
#
#
# But process() expects:
#
# Callable[[str], int]


# Therefore get_name does NOT match
# the expected callback type.


# Expected:
#
# str -> int
#
#
# Received:
#
# int -> str


# ============================================================
# 13. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================================

def calculate(
    a: int,
    b: int
) -> int:

    return a + b


# Here:
#
# a -> int
# b -> int
#
# return -> int


# Therefore:
#
# calculate matches:
#
# Callable[[int, int], int]


# ============================================================
# 14. FUNCTION ACCEPTING A CALLBACK
# ============================================================

def execute(
    a: int,
    b: int,
    operation: Callable[[int, int], int]
) -> int:

    return operation(a, b)


# operation must be a function that:
#
#     accepts int
#     accepts int
#     returns int


# ============================================================
# 15. CALLBACK EXAMPLES
# ============================================================

def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def subtract(a: int, b: int) -> int:
    return a - b


# All three functions match:
#
# Callable[[int, int], int]


# ============================================================
# 16. USING DIFFERENT CALLBACKS
# ============================================================

print(
    execute(
        10,
        20,
        add
    )
)


# Output:
#
# 30


print(
    execute(
        10,
        20,
        multiply
    )
)


# Output:
#
# 200


print(
    execute(
        20,
        10,
        subtract
    )
)


# Output:
#
# 10


# The execute() function stays the same.
#
# Only the callback changes.


# ============================================================
# 17. FUNCTION AS DATA
# ============================================================

def add(a: int, b: int) -> int:
    return a + b


operation: Callable[[int, int], int] = add


# Now:
#
# operation
#
# refers to the add function.


result = operation(10, 20)

print(result)


# Output:
#
# 30


# This demonstrates that functions
# can be stored in variables.


# ============================================================
# 18. CALLBACK WITH NONE RETURN
# ============================================================

def print_name(name: str) -> None:
    print(name)


# This function:
#
# accepts:
#     str
#
# returns:
#     None
#
#
# Therefore its Callable type is:
#
# Callable[[str], None]


def execute_callback(
    callback: Callable[[str], None]
) -> None:

    callback("Alice")


execute_callback(print_name)


# Output:
#
# Alice


# ============================================================
# 19. FUNCTION RETURNING A CALLBACK
# ============================================================

def create_multiplier(
    number: int
) -> Callable[[int], int]:

    def multiply(value: int) -> int:
        return value * number

    return multiply


# The return type:
#
# Callable[[int], int]
#
# means:
#
# create_multiplier() returns a function
# that:
#
#     accepts int
#     returns int


double = create_multiplier(2)


print(double(10))


# Output:
#
# 20


# ============================================================
# 20. TYPE HINTS WITH OPTIONAL RETURN
# ============================================================

def find_student(
    id: int
) -> str | None:

    if id == 1:
        return "Alice"

    return None


# Here:
#
# id -> int
#
# return:
#
# str OR None


# Therefore:
#
# function type:
#
# Callable[[int], str | None]


# ============================================================
# 21. FUNCTION WITH LIST PARAMETER
# ============================================================

def calculate_total(
    numbers: list[int]
) -> int:

    return sum(numbers)


# Type hints:
#
# numbers -> list[int]
#
# return -> int


# Example:

result = calculate_total(
    [10, 20, 30]
)


print(result)


# Output:
#
# 60


# ============================================================
# 22. FUNCTION WITH DICTIONARY PARAMETER
# ============================================================

def get_mark(
    marks: dict[str, int],
    subject: str
) -> int | None:

    return marks.get(subject)


# Type hints:
#
# marks:
#     dict[str, int]
#
# subject:
#     str
#
# return:
#     int OR None


marks: dict[str, int] = {
    "Math": 90,
    "English": 85
}


print(
    get_mark(
        marks,
        "Math"
    )
)


# Output:
#
# 90


print(
    get_mark(
        marks,
        "Physics"
    )
)


# Output:
#
# None


# ============================================================
# 23. FUNCTION WITH TUPLE PARAMETER
# ============================================================

def display_point(
    point: tuple[int, int]
) -> None:

    print(point[0], point[1])


# Type hint:
#
# point -> tuple[int, int]
#
# return -> None


display_point((10, 20))


# Output:
#
# 10 20


# ============================================================
# 24. COMBINING MULTIPLE TYPE HINTS
# ============================================================

def process_student(
    name: str,
    age: int,
    marks: list[int],
    phone: str | None,
    callback: Callable[[str], int]
) -> int:

    return callback(name)


# This function combines:
#
# str
# int
# list[int]
# str | None
# Callable[[str], int]
#
#
# Return:
#
# int


# This demonstrates how type hints
# work together in real applications.


# ============================================================
# 25. TYPE HINTS FOR A REAL FUNCTION
# ============================================================

def find_student_score(
    student_id: int,
    scores: dict[str, int],
    callback: Callable[[str], int]
) -> int | None:

    student_name = "Alice"

    if student_name not in scores:
        return None

    return callback(student_name)


# Type hints:
#
# student_id:
#     int
#
# scores:
#     dict[str, int]
#
# callback:
#     Callable[[str], int]
#
# return:
#     int OR None


# ============================================================
# 26. FUNCTION TYPE HINT STRUCTURE
# ============================================================

def function_name(
    parameter1: type,
    parameter2: type,
    parameter3: type
) -> return_type:
    ...


# General structure:
#
#
# def function_name(
#     parameter: type
# ) -> return_type:
#
#
# parameter:
#     input type
#
# ->
#     output type


# ============================================================
# 27. IMPORTANT FUNCTION TYPE HINT PATTERN
# ============================================================

def add(
    a: int,
    b: int
) -> int:

    return a + b


# Read it as:
#
# add()
#
# accepts:
#
#     a -> int
#     b -> int
#
# returns:
#
#     int


# ============================================================
# 28. FUNCTION WITH CALLBACK
# ============================================================

def execute(
    operation: Callable[[int, int], int],
    a: int,
    b: int
) -> int:

    return operation(a, b)


# Read it as:
#
# operation:
#     function
#     int -> int -> int
#
# a:
#     int
#
# b:
#     int
#
# return:
#     int


# ============================================================
# 29. WHY THIS IS USEFUL
# ============================================================

# Function type hints become especially useful
# in larger applications.
#
#
# They help us understand:
#
#     What arguments does this function accept?
#
#     What does it return?
#
#     Does it accept another function?
#
#     What should that callback accept?
#
#     What should the callback return?
#
#
# This becomes very useful for:
#
#     - Decorators
#     - Callbacks
#     - APIs
#     - Higher-order functions
#     - Function factories
#     - Large Python projects


# ============================================================
# 30. QUICK REFERENCE
# ============================================================

# String parameter, integer return:

def example(name: str) -> int:
    ...


# Integer parameter, string return:

def example(age: int) -> str:
    ...


# List parameter:

def example(numbers: list[int]) -> int:
    ...


# Dictionary parameter:

def example(
    marks: dict[str, int]
) -> int:
    ...


# Optional return:

def example(id: int) -> str | None:
    ...


# Callback:

def example(
    callback: Callable[[str], int]
) -> int:
    ...


# Multiple parameters:

def example(
    name: str,
    age: int
) -> bool:
    ...


# ============================================================
# 31. COMPLETE EXAMPLE
# ============================================================

from typing import Callable


def process(
    name: str,
    age: int,
    callback: Callable[[str], int]
) -> int:

    print("Name:", name)
    print("Age:", age)

    return callback(name)


def get_length(text: str) -> int:
    return len(text)


result = process(
    "Alice",
    20,
    get_length
)


print("Result:", result)


# Output:
#
# Name: Alice
# Age: 20
# Result: 5


# ============================================================
# 32. QUICK SUMMARY
# ============================================================

# Function parameter:

name: str


# Means:
#
# name should be a string.


# Function return type: -> int


# Means:
#
# function should return an integer.


# List parameter:

numbers: list[int]


# Means:
#
# numbers should be a list of integers.


# Optional parameter:

phone: str | None


# Means:
#
# phone can be a string or None.


# Callback parameter:

callback: Callable[[str], int]


# Means:
#
# callback should be a function that:
#
#     accepts a string
#     returns an integer.


# ============================================================
# KEY IDEA
# ============================================================
#
# A fully type-hinted function can describe:
#
#     1. What each parameter accepts
#     2. What type each parameter should have
#     3. Whether a value can be None
#     4. Whether a parameter is another function
#     5. What a callback accepts
#     6. What the callback returns
#     7. What the main function returns
#
#
# Example:
#
# def process(
#     name: str,
#     age: int,
#     callback: Callable[[str], int]
# ) -> int:
#
#
# Means:
#
# name
#     -> str
#
# age
#     -> int
#
# callback
#     -> function
#        accepts str
#        returns int
#
# process()
#     -> returns int
#
#
# This is one of the most useful applications
# of type hints in real Python projects.
#
# ============================================================