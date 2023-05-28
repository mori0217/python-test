s = 'a is {}'.format('a')
print(s)

s = 'a is {}'.format('test')
print(s)

s = 'a is {} {} {}'.format(1, 2, 3)
print(s)

s = 'a is {0} {1} {2}'.format(1, 2, 3)
print(s)

s = 'a is {2} {1} {0}'.format(1, 2, 3)
print(s)

s = 'My name is {0} {1}'.format('a', 'b')
print(s)

s = 'My name is {0} {1}. Go {1} {0}'.format('a', 'b')
print(s)

s = 'My name is {name} {family}. Go {family} {name}'.format(name='aaa', family='bbb')
print(s)

s = str(1)
print(s, type(s))

s = str(3.14)
print(s, type(s))

s = str(True)
print(s, type(s))
