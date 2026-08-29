# This decorator only works for functions with no arguments:
# Python solves this with: def wrapper(*args):
# *args means: "Accept any number of positional arguments."

# Eg 1:
def show(*args):
    print(args)

show(10)
show(10, 20)
show(10, 20, 30)

def show(*args):
    print(args)

show(10, 20, 30)

# output:
# (10, 20, 30)
# Notice the parentheses.
# Because args is a tuple.

def abc(*var):
    print(var)

abc(19)
abc(20)
abc(10,10,90)

