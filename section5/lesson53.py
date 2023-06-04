def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


menu(entree="beef", drink="coffee")

d = {"entree": "beef", "drink": "coffee", "dessert": "ice"}
menu(**d)


def special_menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


special_menu("banana", "apple", "orange", entree="beef", drink="coffee")
