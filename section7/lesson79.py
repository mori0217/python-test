class Person(object):
    def __init__(self, name):
        print("init")
        self.name = name

    def say_something(self):
        print("I am {}.".format(self.name))
        self.run(10)

    def run(self, num):
        print("run" * num)


person = Person("Mike")
person.say_something()
