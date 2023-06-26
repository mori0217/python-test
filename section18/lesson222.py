import contextlib


class tag(contextlib.ContextDecorator):
    def __init__(self, name):
        self.name = name
        self.start_tag = f"<{self.name}>"
        self.end_tag = f"</{self.name}>"

    def __enter__(self):
        print(self.start_tag)

    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type)
        print(exc_value)
        print(traceback)
        print(self.end_tag)


with tag("p"):
    raise Exception("error")
    print("hello")
