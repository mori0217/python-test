import json
import pprint

l = ["apple", "orange", "banana", "peach", "grapes"]
l.insert(0, l[:])

pp = pprint.PrettyPrinter(indent=4, width=40, compact=False, depth=3)
pp.pprint(l)
print(json.dumps(l, indent=4))

d = {"a": "A", "b": "B", "c": {"x": "X", "y": "Y", "z": "Z"}}
pp.pprint(d)
print(json.dumps(d, indent=4))
