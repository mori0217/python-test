import re
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

c = collections.Counter()
l = ["a", "a", "a", "b", "b", "c"]
for word in l:
    c[word] += 1
print(c)
print(c.most_common(2))
print(sum(c.values()))

with open("section18/lesson229.py", "r") as f:
    words = re.findall(r"\w+", f.read().lower())
print(collections.Counter(words))
print(collections.Counter(words).most_common(10))
