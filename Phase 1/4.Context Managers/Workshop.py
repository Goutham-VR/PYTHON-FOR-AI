#basic context manager
with open('data.txt','r') as file:
    data=file.read()

# custom our own context manager
class mycontext:
    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):
        print("exiting")

with mycontext():
    print("Hai")


class ggg:
    def __enter__(self):
        print("hai")

    def __exit__(self, exc_type, exc_value, traceback):
        print("bye")

with ggg():
    print('kkk')

# CONTEXT MANAGER WITH AN ERROR
class ggg:
    def __enter__(self):
        print("hai")

    def __exit__(self, exc_type, exc_value, traceback):
        print("bye")

        print("Exception Type",exc_type)
        print("Exception Value",exc_value)

with ggg():
    print('hai')
    x=10/0

# __exit__ can suppress an exception
class ggg:
    def __enter__(self):
        print('Start')

    def __exit__(self, exc_type, exc, tb):
        print('Exiting')
        return True

with ggg():
    print('Hai')
    x=10/0

# __exit__ RETURNING FALSE / NONE
class ggg:
    def __enter__(self):
        print('Start')

    def __exit__(self, exc_type, exc, tb):
        print('Exiting')
        return False

with ggg():
    print('Hai')
    x=10/0

# __enter__ CAN RETURN A VALUE

class newcalss:
    def __enter__(self):
        print("Entering")
        return "hai"

    def __exit__(self, exc_type, exc, tb):
        print("Exiting")

with newcalss() as value:
    print(value)


class customcm:
    def __enter__(self):
        print("Start")
    def __exit__(self,exc_type,exc_value,traceback):
        print("exit")

with customcm():
    x=10/0
    print("kai")

class customcm:
    def __enter__(self):
        print("Start")
    def __exit__(self,exc_type,exc_value,traceback):
        print("exit")
        print("Exception Type",exc_type)
        print("Exception Value",exc_value)
        
with customcm():
    x=10/0
    print("kai")

class customcm:
    def __enter__(self):
        print("Start")
    def __exit__(self,exc_type,exc_value,traceback):
        print("exit")
        return False

with customcm():
    x=10/0
    print("kai")

class customcm:
    def __enter__(self):
        print("Start")
        return 7
    def __exit__(self,exc_type,exc_value,traceback):
        print("exit")

with customcm() as value:
    print(value)


class dbcontext:
    def __enter__(self):
        print("Connecting To Db")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Closing Database")

    def query(self):
        print("INSERT INTO TBL_DISTRICT.......")

with dbcontext() as db:
    db.query()


class dbconnect:
    def __enter__(self):
        print("connecting to database")
        return self

    def __exit__(self, exc_type, exc, tb):
        print('Closing Databse')

    def query(self):
        return "Query......."

with dbconnect() as db:
    db.query()

from contextlib import contextmanager

@contextmanager
def my_contextd():

    print("Entering")

    yield

    print("Exiting")

with my_contextd():
    print("Inside")