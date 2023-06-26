import functools


def task(f):
    print("task")
    print(f())


def add(x, y):
    return x + y


def add_outer(x, y):
    def add_inner():
        return x + y
    return add_inner


f1 = functools.partial(add, 2, 3)
task(f1)

f2 = add_outer(2, 3)
task(f2)
