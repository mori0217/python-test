import io
import requests
import zipfile

# with open("section18/test.txt", "w") as f:
# f.write("Hello World")

# with open("section18/test.txt", "r") as f:
# print(f.read())

# f = io.StringIO()
# f.write("string io")
# f.seek(0)
# print(f.read())

zip_url = "http://localhost/test.zip"
res = requests.get(zip_url)
f = io.BytesIO()
f.write(res.content)

with zipfile.ZipFile(f) as z:
    with z.open("test.txt") as f:
        print(f.read().decode())
