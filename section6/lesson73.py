import builtins

builtins.print("Hello, World!")

ranking = {"A": 100, "B": 85, "C": 95}

print(sorted(ranking, key=ranking.get, reverse=True))
