import collections
import csv

# p = (10, 20)
# print(p[0])
# # p[0] = 100


# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# p = Point(10, 20)
# print(p.x)

Point = collections.namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x)
# p.x = 100

p1 = Point._make([100, 200])
print(p1)
print(p1._asdict())

p1._replace(x=500)
print(p1)
p2 = p1._replace(x=500)
print(p2)


class SumPoint(collections.namedtuple("Point", ["x", "y"])):
    @property
    def total(self):
        return self.x + self.y


p3 = SumPoint(10, 20)
print(p3.total)

with open("section18/names.csv", "w") as csvfile:
    fieldnames = ["first", "last", "address"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"first": "Mike", "last": "Jackson1", "address": "A"})
    writer.writerow({"first": "Nancy", "last": "Jackson2", "address": "B"})
    writer.writerow({"first": "Linda", "last": "Jackson3", "address": "C"})

with open("section18/names.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    Names = collections.namedtuple("Names", next(reader))
    for row in reader:
        names = Names._make(row)
        print(names.first, names.last, names.address)
