class mycontext:
    def __enter__(self):
        print("Entering")
        return "Values that enter return"
    def __exit__(self, exc_type, exc, tb):
        print("Exiting")

with mycontext() as value:
    print(value)