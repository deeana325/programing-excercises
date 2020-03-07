#33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = 11
b = 9

def sum(a, b):
    if (a+b >= 15) and (a+b <= 20):
        return 20
    else:
        return a+b


print(sum(a, b))