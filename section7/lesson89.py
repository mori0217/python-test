class Person(object):
    kind = "human"

    def __init__(self, name):
        self.name = name

    @classmethod
    def who_are_you(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print("about human {}".format(year))


a = Person("A")
print(a.kind)
print(a.name)
print(a.who_are_you())
a.about(1999)

b = Person
print(b.kind)
# print(b.name)
print(b.who_are_you())
b.about(2023)
