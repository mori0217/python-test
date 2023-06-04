animal = "cat"


def f():
    # global animal
    # print("local before:", animal)
    animal = "dog"
    print("local after:", animal)
    print("locals", locals())
    print("local name", f.__name__)


f()

print("global:", animal)
print("global name", __name__)
# print("globals", globals())
