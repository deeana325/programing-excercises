# 32. Write a Python program to get the least common multiple (LCM) of two positive integers.

a = 4
b = 6


def gcd(a, b):
    while b > 0:
        r = a % b
        a, b = b, r
    return a


def lcm(a, b):
    return a*b/gcd(a, b)


print(lcm(a, b))
