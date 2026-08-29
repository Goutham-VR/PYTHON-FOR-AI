class customcm:
    def __enter__(self):
        print("Start")
        return "Hai"
    def __exit__(self,exc_type,exc_value,traceback):
        print("exit")

with customcm() as value:
    print(value)