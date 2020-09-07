# 25. Write a Python program to check whether a specified value is contained in a group of values.

num = input('comparison value:')
n = int(input('number of values in the list:'))
l = []
for i in range(0, n):
    l.append(input('value:'))
x = False    
for i in l:
    if i == num:
        x = True
if x:
    print('it\'s specified')
else:
    print('it\'s not specified')            