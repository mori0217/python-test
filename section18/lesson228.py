import collections

d = {}
l = ["a", "a", "a", "b", "b", "c"]
for word in l:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(d)

d = {}
l = ["a", "a", "a", "b", "b", "c"]
for word in l:
    d.setdefault(word, 0)
    d[word] += 1
print(d)

d = collections.defaultdict(int)
l = ["a", "a", "a", "b", "b", "c"]
for word in l:
    d[word] += 1
print(d)

d = collections.defaultdict(set)
s = [("red", 1), ("blue", 2), ("red", 3), ("blue", 4), ("red", 1), ("blue", 4)]
for color, value in s:
    d[color].add(value)
print(d)
