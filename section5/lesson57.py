def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")

    return wrapper


def print_more(func):
    def wrapper(*args, **kwargs):
        print("more start")
        func(*args, **kwargs)
        print("more end")

    return wrapper


def add_num(a, b):
    print(a + b)


f = print_info(print_more(add_num))
f(10, 20)


@print_info
def sub_num(a, b):
    print(a - b)


sub_num(100, 10)


@print_info
@print_more
def multiple_num(a, b):
    print(a * b)


multiple_num(3, 4)
