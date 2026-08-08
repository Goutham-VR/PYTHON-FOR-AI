def deco(func):
    def wrapper(*args): # wrapper function is the enhanced function
        print("Start")
        func(*args) # Call the original function with the arguments passed to the wrapper
        print("End") 
    return wrapper

@deco
def add(a,b):
    print(a+b)

add(10,20)