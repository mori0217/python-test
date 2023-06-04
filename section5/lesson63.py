def g():
    for i in range(10):
        if i % 2 == 0:
            yield i


for i in g():
    print(i)

g2 = (i for i in range(10) if i % 2 == 0)
for x in g2:
    print(x)
