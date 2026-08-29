def add(a:int,b:int) -> int:
    return a+b

print(add(2,3))

def add(a:int,b:int) -> str:
    return a+b

data=add(2,3)
print(type(data))

def add(a: int, b: int) -> int:
    return a + b

add("Hello", "World")

numbers: list[int] = [10, 20, 30]

def list(numbers:list[int]) -> int:
    return sum(numbers)

nos=[1,2,3,4,5,6]
result=list(nos)
print(result)