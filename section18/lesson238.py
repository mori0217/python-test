import datetime

s = "test"
print(s)
print(str(s))
print(repr(s))

d = datetime.datetime.now()
print(d)
print(str(d))
print(repr(d))

print("{!r}".format(s))
print("{!s}".format(s))
print("{}".format(s))


class Point(object):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "Point(x={}, y={})".format(self.x, self.y)

    # def __repr__(self) -> str:
        # return "Point Test"


p = Point(1, 2)
print("{0!r}".format(p))
print("{0!s}".format(p))
print("{}".format(p))
