s = ['a', 'b', 'c', 'd', 'e', 'f' , 'g']
print(s[0])
s[0] = 'A'
print(s)
print(s[2:5])
s[2:5] = ['C', 'D', 'E']
print(s)
s[2:5] = []
print(s)
print(s[:])
s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n.append(100)
print(n)
n.insert(0, 200)
print(n)
print(n.pop())
print(n)
print(n.pop(0))
print(n)
del n[0]
print(n)
del n

n = [1, 2, 2, 2, 3]
n.remove(2)
print(n)
n.remove(2)
print(n)
n.remove(2)
print(n)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8 , 9, 10]
c = a + b
print(c)
a += b
print(a)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8 , 9, 10]
x.extend(y)
print(x)