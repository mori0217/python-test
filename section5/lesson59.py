l = ["a", "b", "c"]
for i in l:
    print(i)


def generate_abc():
    yield "a"
    yield "b"
    yield "c"


g = generate_abc()
print(next(g))
print(next(g))
print(next(g))


def generate_abc2():
    yield "a2"
    yield "b2"
    yield "c2"


for i in generate_abc2():
    print(i)


def counter(num=10):
    for _ in range(num):
        print("prepare")
        yield "run"


for i in counter():
    print(i)
