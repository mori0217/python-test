with open("section8/test.txt", "r") as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
