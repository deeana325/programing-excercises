# 22. Write a Python program to count the number 4 in a given list.

l = []
n = int(input('number of list elements:'))
for i in range(n):
    l.append(int(input('number:')))
# print('there are', l.count(4), '4\'s in the list')

count = 0
for x in l:
    if x == 4:
        count = count + 1
print('count =', count)        

