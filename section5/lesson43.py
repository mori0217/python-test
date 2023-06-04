for fruit in ["apple", "banana", "orange"]:
    print(fruit)
else:
    print("I ate all.")

for fruit in ["apple", "banana", "orange"]:
    if fruit == "banana":
        print("stop eating.")
        break
    print(fruit)
else:
    print("I ate all.")
