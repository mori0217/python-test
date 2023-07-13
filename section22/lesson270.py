def g_hello():
    yield 'hello1'
    yield 'hello2'
    yield 'hello3'


# for i in g_hello():
#     print(i)

g = g_hello()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))


def g_world():
    while True:
        r = yield "world"
        yield r


g = g_world()
print(next(g))
print(g.send('mike'))
print(next(g))
print(g.send('nancy'))
