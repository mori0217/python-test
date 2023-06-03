t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))
print(t[0])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.index(1, t.index(1) + 1))
print(t.count(1))

t = ([1, 2, 3], [4, 5, 6])
print(t[0][0])
t[0][0] = 100
print(t)

t = 1, 2, 3
print(type(t))
t = 1,
print(type(t))

new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)

new_tuple = (1,) + (4, 5, 6)
print(new_tuple)