def s_hello():
    yield 'hello1'
    yield 'hello2'
    yield 'hello3'
    return "done"


def g_hello():
    while True:
        r = yield from s_hello()
        yield r


g = g_hello()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
