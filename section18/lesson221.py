import contextlib


# def tag(name):
#     def decorator(func):
#         def wrapper(content):
#             print(f"<{name}>")
#             r = func(content)
#             print(f"</{name}>")
#             return r
#         return wrapper
#     return decorator


# @tag("p")
# def f(content):
#     print(content)


# # f = tag("p")(f)

# f("hello")

@contextlib.contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")


@tag("p")
def f(content):
    print(content)


f("hello")


def f2():
    print("hello")
    with tag("p"):
        print("world")
        with tag("h"):
            print("python")


f2()
