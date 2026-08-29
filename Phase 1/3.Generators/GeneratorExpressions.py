list1=[x*x for x in range(10)] # called list comprehension created in memory at once
print(list1)

list2=[x+x for x in range(10)]
print(list2)

# For Generator Expression
# Just change the square brackets [] to parentheses ().

numbers=(x*x for x in range(10))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# another method using for loop
numbers=(x*x for x in range(10))
for i in numbers:
    print(i)

# generator remeber its state
nums = (x * 2 for x in range(5))

print(next(nums)) # output 0
print(next(nums)) # output 2

for n in nums:
    print(n)

# output 4, 6, 8 
# A generator remembers its state.
# It doesn't restart unless you create a new generator.