from lesson_package import utils

# from .. import utils


def sing():
    return "aaaaaaa"


def cry():
    return utils.say_twice("bbbbbbb")


if __name__ == "__main__":
    print(sing())
    print("animal:", __name__)
