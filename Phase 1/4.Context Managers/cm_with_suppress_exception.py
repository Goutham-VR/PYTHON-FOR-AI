class mycontext:
    def __enter__(self):
        print("Entering")
    def __exit__(self, exc_type, exc, tb):
        print("Exiting")
        return True

# Test one with no error
with mycontext():
    print("Main Content")

#test with an error
with mycontext():
    print("Main Content")
    x=10/0
