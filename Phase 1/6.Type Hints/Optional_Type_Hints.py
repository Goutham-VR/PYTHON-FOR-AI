# ============================================================
# TYPE HINTS IN PYTHON
# PART 5: OPTIONAL TYPE HINTS
# ============================================================


# ============================================================
# 1. WHAT IS OPTIONAL?
# ============================================================

# Sometimes a value may exist,
# and sometimes it may not exist.
#
# In Python, we commonly represent
# "no value" using:
#
# None


# Example:

phone: str | None = None


# This means:
#
# phone can contain:
#
#     str
# OR
#     None
#
#
# So:
#
# "9876543210" -> valid
# None         -> valid


# ============================================================
# 2. STRING OR NONE
# ============================================================

phone: str | None = "9876543210"


# Valid because:
#
# "9876543210" -> str


phone: str | None = None


# Also valid because:
#
# None -> allowed


# But:

phone: str | None = 12345


# Not the expected type because:
#
# 12345 -> int
#
# Allowed:
#
# str
# None
#
# Not allowed:
#
# int


# ============================================================
# 3. WHAT DOES | MEAN?
# ============================================================

phone: str | None


# The | symbol means:
#
# OR
#
#
# Therefore:
#
# str | None
#
# means:
#
# string OR None


# Another example:

value: int | str


# Means:
#
# value can be:
#
# int
# OR
# str


# Example:

value: int | str = 100

value: int | str = "Hello"


# Both are valid.


# ============================================================
# 4. NONE IS A SPECIAL VALUE
# ============================================================

phone = None


# None means:
#
# There is currently no value.
#
# It does NOT mean:
#
# 0
#
# ""
#
# False
#
#
# These are different values.


# Example:

phone = None

age = 0

name = ""

active = False


# These all represent different things.


# ============================================================
# 5. FUNCTION RETURNING OPTIONAL VALUE
# ============================================================

def find_student(id: int) -> str | None:
    if id == 1:
        return "Alice"

    return None


# There are two type hints here:
#
#
# id: int
#
# means:
#
# id should be an integer.
#
#
# -> str | None
#
# means:
#
# the function can return:
#
# str
# OR
# None


# ============================================================
# 6. CALLING THE FUNCTION
# ============================================================

result = find_student(1)

print(result)


# Output:
#
# Alice


# Why?
#
# id == 1
#
# Therefore:
#
# return "Alice"


# ============================================================
# 7. STUDENT NOT FOUND
# ============================================================

result = find_student(10)

print(result)


# Output:
#
# None


# Why?
#
# id != 1
#
# Therefore:
#
# return None


# ============================================================
# 8. IMPORTANT: CHECKING FOR NONE
# ============================================================

student = find_student(10)


if student is not None:
    print(student)
else:
    print("Student not found")


# Output:
#
# Student not found


# This is a very common pattern
# when working with optional values.


# ============================================================
# 9. WHY USE is NOT None?
# ============================================================

student = find_student(1)


if student is not None:
    print("Student:", student)


# We use:
#
# is not None
#
# rather than:
#
# != None
#
#
# The recommended Python style is:
#
# value is None
#
# or:
#
# value is not None


# ============================================================
# 10. OPTIONAL FUNCTION PARAMETER
# ============================================================

def greet(name: str | None) -> None:

    if name is not None:
        print("Hello", name)
    else:
        print("Hello Guest")


# name can be:
#
# str
# OR
# None


greet("Alice")


# Output:
#
# Hello Alice


greet(None)


# Output:
#
# Hello Guest


# ============================================================
# 11. OPTIONAL PARAMETER WITH DEFAULT VALUE
# ============================================================

def greet(name: str | None = None) -> None:

    if name is not None:
        print("Hello", name)
    else:
        print("Hello Guest")


# Here:
#
# name -> str | None
#
# Default value:
#
# None


# Therefore these are valid:

greet()

greet("Alice")

greet(None)


# ============================================================
# 12. OPTIONAL VALUE IN A CLASS
# ============================================================

class Student:

    def __init__(
        self,
        name: str,
        phone: str | None
    ):
        self.name = name
        self.phone = phone


# A Student can have:
#
# name:
#     str
#
# phone:
#     str OR None


student1 = Student(
    "Alice",
    "9876543210"
)


student2 = Student(
    "John",
    None
)


# Both are valid.


# ============================================================
# 13. OPTIONAL ATTRIBUTE
# ============================================================

class Student:

    def __init__(self, name: str):
        self.name: str = name
        self.phone: str | None = None


# Initially:
#
# phone = None
#
#
# Later we can assign a phone number:

student = Student("Alice")

student.phone = "9876543210"


# Now:
#
# student.phone -> str


# ============================================================
# 14. OPTIONAL WITH LIST
# ============================================================

phone_numbers: list[str] | None = None


# This means:
#
# phone_numbers can be:
#
# list[str]
# OR
# None


# Example:

phone_numbers = ["9876543210", "9123456780"]


# Also valid:

phone_numbers = None


# ============================================================
# 15. OPTIONAL WITH DICTIONARY
# ============================================================

student: dict[str, int] | None = None


# This means:
#
# student can be:
#
# dict[str, int]
# OR
# None


student = {
    "Math": 90,
    "English": 85
}


# Valid.


student = None


# Also valid.


# ============================================================
# 16. OPTIONAL WITH TUPLE
# ============================================================

point: tuple[int, int] | None = None


# Means:
#
# point can be:
#
# tuple[int, int]
# OR
# None


point = (10, 20)


# Valid.


point = None


# Also valid.


# ============================================================
# 17. DATABASE EXAMPLE
# ============================================================

def get_student(id: int) -> str | None:

    if id == 1:
        return "Alice"

    return None


# Imagine this function searches a database.
#
# If the student exists:
#
# return student name
#
#
# If the student does not exist:
#
# return None


student = get_student(1)


if student is not None:
    print("Found:", student)
else:
    print("Student not found")


# Output:
#
# Found: Alice


# ============================================================
# 18. API EXAMPLE
# ============================================================

def get_email(user_id: int) -> str | None:

    # Imagine API/database lookup here.

    if user_id == 1:
        return "alice@example.com"

    return None


# The API may return:
#
# "alice@example.com"
#
# OR:
#
# None
#
# if the email does not exist.


# ============================================================
# 19. OLDER PYTHON STYLE: Optional
# ============================================================

from typing import Optional


phone: Optional[str] = None


# This means exactly the same thing as:
#
# phone: str | None = None


# Modern Python:
#
# str | None
#
# Older/common style:
#
# Optional[str]


# ============================================================
# 20. OPTIONAL VS REQUIRED
# ============================================================

# This variable must contain a string:

name: str = "Alice"


# This variable can contain a string
# or no value:

phone: str | None = None


# Therefore:
#
# str
#     -> string is expected
#
#
# str | None
#     -> string OR no value


# ============================================================
# 21. IMPORTANT: OPTIONAL DOES NOT MEAN OPTIONAL ARGUMENT
# ============================================================

def greet(name: str | None) -> None:
    print(name)


# The type hint says:
#
# name can be str OR None.
#
# But the argument is still required when calling
# the function.


greet("Alice")


greet(None)


# But:

greet()


# This is NOT valid because name was not provided.


# If we want the argument itself to be optional,
# we give it a default value:


def greet(name: str | None = None) -> None:
    print(name)


# Now this is valid:

greet()

greet("Alice")

greet(None)


# Important distinction:
#
# str | None
#     -> value can be None
#
#
# = None
#     -> argument has a default value
#        and can be omitted


# ============================================================
# 22. QUICK REFERENCE
# ============================================================

# String or None:

str | None


# Integer or None:

int | None


# Float or None:

float | None


# Boolean or None:

bool | None


# List of integers or None:

list[int] | None


# Dictionary or None:

dict[str, int] | None


# Tuple or None:

tuple[int, int] | None


# ============================================================
# 23. OLD STYLE VS MODERN STYLE
# ============================================================

from typing import Optional


# Older style:

phone: Optional[str] = None


# Modern style:

phone: str | None = None


# Both mean:
#
# phone can be a string or None.


# ============================================================
# 24. QUICK SUMMARY
# ============================================================

# str | None
#     -> string OR None
#
#
# int | None
#     -> integer OR None
#
#
# list[int] | None
#     -> list of integers OR None
#
#
# dict[str, int] | None
#     -> dictionary OR None
#
#
# tuple[int, int] | None
#     -> tuple OR None


# Function:

def find_student(id: int) -> str | None:
    ...


# Means:
#
# id:
#     int
#
# return:
#     str OR None


# ============================================================
# KEY IDEA
# ============================================================
#
# None represents the absence of a value.
#
#
# str | None
#
# means:
#
#     string OR no value
#
#
# This is extremely common in real applications.
#
# Examples:
#
#     Database search
#     API response
#     User profile
#     Phone number
#     Email address
#     Optional configuration
#     Missing data
#
#
# Remember:
#
# int
#     -> integer
#
# str
#     -> string
#
# None
#     -> no value
#
# str | None
#     -> string OR no value
#
# int | None
#     -> integer OR no value
#
# ============================================================