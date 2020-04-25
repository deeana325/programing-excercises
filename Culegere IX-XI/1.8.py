

a = input('a =')
b = input('b =')
c = input('c =')
v = [a, b, c]

print(v)
v.insert(0, v.pop())
print(v)