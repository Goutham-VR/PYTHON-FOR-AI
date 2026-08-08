# keyword yield is used to create a generator function instead of return.
# A generator function is a special type of function that returns an iterator object.
# It allows you to iterate over a sequence of values without storing them all in memory at once.

# Eg 1: Normal Function
def numbers():
    return [1, 2, 3]

print(numbers())

# output: [1, 2, 3]

# Eg 2: Generator Function
def numbers():
    yield 1
    yield 2
    yield 3

print(numbers())

# output : <generator object numbers at 0x...>
# why?
# Because yield doesn't execute the whole function immediately.
# It creates a generator object.

# getting values from the generator object using next() function
def numbers():
    yield 1
    yield 2
    yield 3

g = numbers()

print(next(g)) # output: 1
print(next(g)) # output: 2
print(next(g)) # output: 3
print(next(g)) # output: StopIteration error because there are no more values to yield.

# Difference Between return and yield
def test():
    return 1
    return 2

# output: 1 
# The function ends immediately after the first return.

def test():
    yield 1
    yield 2

t=test()
print(next(t)) # output: 1
print(next(t)) # output: 2

# The function pauses after each yield and continues from the same place when next() is called again.

n=10
def numbers():
    for i in range(1,n):
        yield i

d=numbers()

for i in range(n):
    print(next(d)) # output: 0 1 2 3 4 5 6 7 8 9


# Why not just use return?
# Suppose you want numbers from 1 to 1,000,000.
# Using return Python creates 1 million numbers in memory before returning them.
# Using yield One number at a time.
# This is why generators are memory efficient.

# AI Example
# Imagine you have:10,000,000 retina images
# You don't want to load all 10 million images into RAM.

# def image_loader():
#     for image in dataset:
#         yield image

# Training does:
# for img in image_loader():
#     train(img)

# This is exactly how many deep learning pipelines work.

def counter():
    for i in range(3):
        print(f"Generating {i}")
        yield i

g = counter()

print(next(g))
print(next(g))

# One Last Important Thing: for Loop with Generators
# Until now you've used: next(g), But in real code, we usually don't call next() manually.
# Instead:
def counter():
    for i in range(3):
        yield i

for num in counter():
    print(num)

# output:
# 0
# 1
# 2

# The for loop secretly does something like this:
g = counter()

while True:
    try:
        value = next(g)
        print(value)
    except StopIteration:
        break

# You don't write this yourself—the for loop handles next() and StopIteration automatically.
# This is why generators are so convenient.