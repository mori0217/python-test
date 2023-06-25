import collections

a = {"a": "a", "c": "c", "num": 0}
b = {"b": "b", "c": "c"}
c = {"b": "bbb", "c": "ccc"}

# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)

m = collections.ChainMap(a, b, c)
print(m)
print(m.maps)
print(m["c"])

m.maps.reverse()
print(m.maps)
print(m["c"])

m.maps.insert(0, {"c": "CCCC"})
print(m.maps)
print(m["c"])

del m.maps[0]
print(m.maps)
print(m["c"])

m["b"] = "BBBB"
print(m.maps)
print(m["b"])


class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                if type(mapping[key]) is int and mapping[key] < value:
                    mapping[key] = value
                return
        self.maps[0][key] = value


m = DeepChainMap(a, b, c)
print(m)
m["num"] = 1
print(m)
m["num"] = -1
print(m)
m["new_num"] = 2
print(m)
