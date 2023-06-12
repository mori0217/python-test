with open("section8/test.txt", "r") as f:
    while True:
        line = f.readline()
        print(line, end="")
        if not line:
            break

print("")

with open("section8/test.txt", "r") as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break
