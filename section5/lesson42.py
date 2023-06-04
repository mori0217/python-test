some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

for i in some_list:
    print(i)

for s in "abcde":
    print(s)

for word in ["a", "b", "c", "d", "e"]:
    if word == "c":
        break
    print(word)

for word in ["a", "b", "c", "d", "e"]:
    if word == "c":
        continue
    print(word)
