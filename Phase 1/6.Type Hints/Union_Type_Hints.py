# ============================================================
# TYPE HINTS IN PYTHON
# PART 6: UNION TYPE HINTS
# ============================================================


# ============================================================
# 1. WHAT IS UNION?
# ============================================================

# Sometimes a variable can contain
# more than one possible type.
#
# Example:

value = 10


# But the same variable might also contain:

value = "Ten"


# We can describe both possibilities
# using a Union type hint.


# ============================================================
# 2. UNION USING typing.UNION
# ============================================================

from typing import Union


value: Union[int, str]


# This means:
#
# value can be:
#
#     int
# OR
#     str


# Therefore these are valid:

value: Union[int, str] = 10

value: Union[int, str] = "Ten"


# ============================================================
# 3. MODERN UNION SYNTAX
# ============================================================

# Modern Python allows:

value: int | str


# This means exactly the same thing as:

value: Union[int, str]


# So:

Union[int, str]


# and:

int | str


# both mean:
#
# integer OR string.


# Modern syntax is usually:
#
#     shorter
#     cleaner
#     easier to read


# ============================================================
# 4. UNION WITH TWO TYPES
# ============================================================

value: int | str = 100


# Valid because:
#
# 100 -> int


value: int | str = "Hello"


# Also valid because:
#
# "Hello" -> str


# But:

value: int | str = 10.5


# Not expected because:
#
# 10.5 -> float
#
# Allowed types:
#
# int
# str
#
# float is not included.


# ============================================================
# 5. UNION WITH MULTIPLE TYPES
# ============================================================

value: int | float | str


# This means:
#
# value can be:
#
#     int
# OR
#     float
# OR
#     str


# Examples:

value: int | float | str = 100

value: int | float | str = 10.5

value: int | float | str = "Hello"


# All three match the type hint.


# ============================================================
# 6. UNDERSTANDING THE | SYMBOL
# ============================================================

value: int | float | str


# The | symbol means OR.
#
#
# Therefore:
#
# int | float | str
#
# means:
#
# int
# OR
# float
# OR
# str


# You can think of it as:
#
# int OR float OR str


# ============================================================
# 7. FUNCTION PARAMETER WITH UNION
# ============================================================

def process(value: int | str) -> str:
    return str(value)


# The parameter:
#
# value: int | str
#
# means:
#
# value can be an integer
# OR
# value can be a string.
#
#
# The return type:
#
# -> str
#
# means:
#
# the function returns a string.


# ============================================================
# 8. CALLING THE FUNCTION
# ============================================================

result = process(100)

print(result)


# Output:
#
# 100
#
# The input:
#
# 100 -> int
#
# is allowed.


result = process("Hello")

print(result)


# Output:
#
# Hello
#
# The input:
#
# "Hello" -> str
#
# is also allowed.


# ============================================================
# 9. UNION DOES NOT MEAN MULTIPLE VALUES
# ============================================================

value: int | str


# This does NOT mean:
#
# value contains an int AND a str
#
#
# It means:
#
# value can contain:
#
# int OR str
#
# at a particular time.


# Example:

value: int | str = 100


# At this moment:
#
# value -> int


value = "Hello"


# Now:
#
# value -> str


# ============================================================
# 10. UNION WITH NONE
# ============================================================

value: int | None = None


# This means:
#
# value can be:
#
#     int
# OR
#     None


value = 100


# Valid.


value = None


# Also valid.


# ============================================================
# 11. UNION WITH OPTIONAL
# ============================================================

from typing import Optional


value: Optional[int]


# This is an older/common way of writing:

value: int | None


# Therefore:
#
# Optional[int]
#
# means:
#
# int OR None


# Another example:

name: Optional[str]


# Means:
#
# str OR None


# Modern version:

name: str | None


# ============================================================
# 12. UNION VS OPTIONAL
# ============================================================

# Union of two normal types:

value: int | str


# Means:
#
# int OR str


# Optional string:

name: str | None


# Means:
#
# str OR None


# Optional integer:

age: int | None


# Means:
#
# int OR None


# So:
#
# Optional is basically a special case
# of Union involving None.


# ============================================================
# 13. FUNCTION WITH MULTIPLE RETURN TYPES
# ============================================================

def get_value() -> int | float | None:
    ...


# This means the function can return:
#
#     int
# OR
#     float
# OR
#     None


# Therefore there are 3 possible return types.


# ============================================================
# 14. COMPLETE FUNCTION EXAMPLE
# ============================================================

def get_value(option: int) -> int | float | None:

    if option == 1:
        return 10

    if option == 2:
        return 10.5

    return None


# Possible results:
#
#
# get_value(1)
#
# -> 10
# -> int
#
#
# get_value(2)
#
# -> 10.5
# -> float
#
#
# get_value(3)
#
# -> None
# -> None


# ============================================================
# 15. CHECKING THE RETURN VALUE
# ============================================================

result = get_value(1)


if result is not None:
    print(result)


# Output:
#
# 10


# If:

result = get_value(3)


# result will be:
#
# None


# So we can check:

if result is None:
    print("No value found")


# Output:
#
# No value found


# ============================================================
# 16. UNION WITH LIST
# ============================================================

value: list[int] | str


# This means:
#
# value can be:
#
#     list[int]
# OR
#     str


value: list[int] | str = [10, 20, 30]


# Valid.


value = "Hello"


# Also valid.


# ============================================================
# 17. UNION WITH DICTIONARY
# ============================================================

data: dict[str, int] | None = None


# Means:
#
# data can be:
#
#     dict[str, int]
# OR
#     None


data = {
    "Math": 90,
    "English": 85
}


# Valid.


data = None


# Also valid.


# ============================================================
# 18. UNION WITH TUPLE
# ============================================================

data: tuple[int, int] | str


# Means:
#
# data can be:
#
#     tuple[int, int]
# OR
#     str


data = (10, 20)


# Valid.


data = "Point"


# Also valid.


# ============================================================
# 19. OLD STYLE UNION
# ============================================================

from typing import Union


value: Union[int, float, str]


# This means:
#
# int
# OR
# float
# OR
# str


# Modern equivalent:

value: int | float | str


# The modern version is generally easier to read.


# ============================================================
# 20. UNION IN REAL APPLICATIONS
# ============================================================

def convert(value: int | float | str) -> str:
    return str(value)


# This can accept:
#
# integer
# float
# string


convert(100)

convert(10.5)

convert("Hello")


# All are allowed by the type hint.


# ============================================================
# 21. UNION IN DATABASE FUNCTIONS
# ============================================================

def find_student(id: int) -> str | None:

    if id == 1:
        return "Alice"

    return None


# Possible return values:
#
# "Alice" -> str
#
# None     -> None
#
#
# This is a Union:
#
# str | None


# ============================================================
# 22. UNION IN API FUNCTIONS
# ============================================================

def get_score(user_id: int) -> int | float | None:

    if user_id == 1:
        return 95

    if user_id == 2:
        return 95.5

    return None


# Possible return types:
#
# int
# float
# None


# This is useful when an API or database
# may return different kinds of values.


# ============================================================
# 23. QUICK REFERENCE
# ============================================================

# Integer OR string:

int | str


# Integer OR float:

int | float


# Integer OR float OR string:

int | float | str


# String OR None:

str | None


# Integer OR None:

int | None


# List of integers OR string:

list[int] | str


# Dictionary OR None:

dict[str, int] | None


# Tuple OR string:

tuple[int, int] | str


# ============================================================
# 24. UNION VS SINGLE TYPE
# ============================================================

# Single type:

value: int


# Only int is expected.


# Union:

value: int | str


# int OR str is expected.


# Multiple types:

value: int | float | str


# int OR float OR str is expected.


# ============================================================
# 25. IMPORTANT: UNION DESCRIBES POSSIBILITIES
# ============================================================

def get_value() -> int | float | None:
    ...


# This does NOT mean the function returns
# three values at the same time.
#
# It means the function can return
# one of these types depending on the situation.
#
#
# Possible result:
#
# 10
#
# OR:
#
# 10.5
#
# OR:
#
# None


# ============================================================
# 26. QUICK SUMMARY
# ============================================================

# Union using older syntax:

Union[int, str]


# Modern syntax:

int | str


# Both mean:
#
# int OR str


# Multiple types:

int | float | str


# Means:
#
# int
# OR
# float
# OR
# str


# Optional:

str | None


# Means:
#
# str
# OR
# None


# Older Optional syntax:

Optional[str]


# Means the same as:
#
# str | None


# ============================================================
# KEY IDEA
# ============================================================
#
# Union allows a type hint to describe
# multiple possible types.
#
#
# Example:
#
# int | str
#
# means:
#
# integer OR string
#
#
# Example:
#
# int | float | str
#
# means:
#
# integer OR float OR string
#
#
# Example:
#
# int | float | None
#
# means:
#
# integer OR float OR no value
#
#
# Remember:
#
# | means OR
#
#
# Union[int, str]
#     ↓
# int | str
#
# The modern syntax is shorter and easier to read.
#
# ============================================================