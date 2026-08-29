#A decorator modifies or adds behavior to a function or method without changing its original code.
# Original Function
#         ↓
# Decorator
#         ↓
# Enhanced Function

# Eg 1:
def mydecorator(func): # decorator function
    def wrapper(): # wrapper function is the enhanced function
        print("Before Function")

        func()

        print("After Function")

    return wrapper

@mydecorator # This is equivalent to greet=mydecorator(greet)
def greet(): 
    print("Hello")

# greet=mydecorator(greet) # this is equivalent to greet() being passed to mydecorator and the returned wrapper function being assigned back to greet

greet() # greet is now enhanced by the decorator

# Eg 2:
def deco(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@deco
def test():
    print("Python")

test()

# Eg 3:
def decorgoutham(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper

@decorgoutham
def gouthamfunction():
    print("Hello Goutham")

gouthamfunction()

# Eg 4:
def decorfunction(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function") 
    return wrapper

@decorfunction
def myfunction():
    print("Hello World")

myfunction()

# Eg 5:
def deco(func):
    def wrapper(name):
        print("Start")
        func(name)
        print("End")
    return wrapper

@deco
def greet(name):
    print(f"Hello {name}")

greet("Alice")
