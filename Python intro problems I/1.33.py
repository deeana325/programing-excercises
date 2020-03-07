#33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = 19
b = 1
c = 12

def sum3(a, b, c):
    if (a == b) or (b == c) or (a == c):
        return 0
    else:
        return a + b + c


print(sum3(a, b, c))
print(sum([a, b, c]))