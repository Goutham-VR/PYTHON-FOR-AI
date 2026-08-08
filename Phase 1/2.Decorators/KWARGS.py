# Keyword arguments have a name=value format:
# **var collects keyword arguments into a dictionary.
def abc(**var):
    print(var)


abc(name="Goutham")
abc(age=23)
abc(name="Goutham", age=23)


# Eg 1:
def show(**kwargs):
    print(kwargs)

show(name="Alice", age=25)


# Eg 2:
def show(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])

show(name="Alice", age=25)

#Example 3: Loop Through Dictionary
def show(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

show(name="Alice", age=25, city="Kochi")

# Example 4: Mixing Normal Parameters and **kwargs
def student(course, **kwargs):
    print("Course:", course)
    print(kwargs)

student("Python", name="Alice", age=25)

# Example 5: Inside a Decorator
def deco(func):
    def wrapper(*args, **kwargs):
        print("Before")

        func(*args, **kwargs)

        print("After")

    return wrapper

@deco
def student(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student(name="Alice", age=25)