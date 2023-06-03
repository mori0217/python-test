d = {"x": 10, "y": 20}
print(d.keys())
print(d.values())

d2 = {"x": 1000, "j": 500}
d.update(d2)
print(d)
print(d["x"])
print(d.get("x"))
r = d.get("z")
print(r)
print(type(r))
print(d.pop("x"))
print(d)
del d["y"]
print(d)
del d

d = {"x": 10, "y": 20}
d.clear()
print(d)


d = {"x": 10, "y": 20}
is_x = "x" in d
print(is_x)
is_j = "j" in d
print(is_j)
