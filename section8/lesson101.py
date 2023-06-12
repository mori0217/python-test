import tempfile

with tempfile.TemporaryFile(mode="w+") as temp:
    temp.write("Some data")
    temp.seek(0)
    print(temp.read())

with tempfile.NamedTemporaryFile(delete=False) as temp:
    print(temp.name)
    with open(temp.name, "w+") as f:
        f.write("Some data to temp file")
        f.seek(0)
        print(f.read())

with tempfile.TemporaryDirectory() as temp:
    print(temp)

temp = tempfile.mkdtemp()
print(temp)
