def say_something():
    return "hi"


result = say_something()
print(result)


def what_is_this(color):
    if color == "red":
        return "tomato"
    elif color == "green":
        return "green pepper"
    else:
        return "I don't know"


print(what_is_this("red"))
print(what_is_this("green"))
print(what_is_this("blue"))
