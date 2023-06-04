def outer(a, b):
    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    return r1 + r2


print(outer(1, 2))
