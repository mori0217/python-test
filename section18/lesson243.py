import functools


def d(f):
    @functools.wraps(f)
    def w():
        """wrapper function"""
        print("decorator")
        f()
    return w


@d
def example():
    """example function"""
    print("example")


example()
print(example.__doc__)
# help(example)
