import collections


d = {"apple": 1, "banana": 2, "orange": 3, "melon": 4}

od1 = collections.OrderedDict(
    {"apple": 1, "banana": 2, "orange": 3, "melon": 4}
)
od2 = collections.OrderedDict(
    {"banana": 2, "apple": 1, "orange": 3, "melon": 4}
)

print(od1 == od2)
print(d == od1)
print(d == od2)

od = collections.OrderedDict(sorted(d.items(), key=lambda t: -t[1]))
print(od)
od["pineapple"] = 5
print(od)
od = collections.OrderedDict(sorted(od.items(), key=lambda t: -t[1]))
print(od)
