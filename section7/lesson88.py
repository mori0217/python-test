class Person(object):
    kind = "human"

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person("A")
b = Person("B")
a.who_are_you()
b.who_are_you()


class T(object):
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word("add 1")
c.add_word("add 2")
d = T()
d.add_word("add 3")
d.add_word("add 4")

print(c.words)
print(d.words)
