import abc


class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception("No drive")


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print("OK")


class Car(object):
    def __init__(self, model=None):
        self.model = model
        print("init model={}".format(self.model))

    def run(self):
        print("run")

    def ride(self, person):
        person.drive()


baby = Baby()
adult = Adult()
car = Car()
car.ride(adult)
car.ride(baby)
