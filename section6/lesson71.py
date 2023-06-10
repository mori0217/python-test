try:
    from lesson_package.talk import utils
except ImportError:
    from lesson_package import utils

print(utils.say_twice("word"))
