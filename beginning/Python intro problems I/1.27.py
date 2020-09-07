# 27. Write a Python program to concatenate all elements in a list into a string and return it.

n = int(input('number of list elements:'))
l = []
for i in range(0, n):
    l.append(input('element:'))
s = ''    
for i in l:
    s = s + str(i)
print(s)

