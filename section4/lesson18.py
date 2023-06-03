r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, r.index(3)+1))
print(r.count(3))

if 5 in r:
    print('exist 5')

if 100 in r:
    print('exist 100')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'a b c d e'
to_split = s.split(' ')
print(to_split)
s = ' '.join(to_split)
print(s)
