def menu(entree="beef", drink="wine", dessert="ice"):
    print("entree = ", entree)
    print("drink = ", drink)
    print("dessert = ", dessert)


menu()
menu("chicken")
menu("chicken", "beer", "cake")
menu(entree="chicken", drink="beer", dessert="cake")
menu(entree="chicken", dessert="cake", drink="beer")
menu("fish", drink="beer", dessert="ice")
