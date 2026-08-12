from contextlib import contextmanager


@contextmanager
def my_contextd():

    print("Entering")

    yield

    print("Exiting")

with my_contextd():
    print("Inside")


#contextmanager WITH A VALUE
@contextmanager
def mycontext():
    print("Entering")
    yield "Hai"
    print("Exiting")

with mycontext() as a:
    print(a)

@contextmanager
def mycontext():
    print("Entering")
    yield "Hai"
    print('Exiting')

with mycontext() as a:
    print(a)

@contextmanager
def mycontext():
    print("Print Accured")
    try:
        yield
    finally:
        print("Print Cleanup")

with mycontext():
    print("Hai")