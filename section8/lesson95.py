s = """\
AAA
BBB
CCC
DDD\
"""
with open("section8/test.txt", "w+") as f:
    f.write(s)
    f.seek(0)
    print(f.read())

with open("section8/test.txt", "r+") as f:
    print(f.read())
    f.seek(0)
    f.write(s)
