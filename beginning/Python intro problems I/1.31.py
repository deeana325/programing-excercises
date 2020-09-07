# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

a = 45 * 1337
b = 74 * 1128


def gcd(a, b):
    j = 0
    for i in range(int(min(a, b)/2), 0, -1):
        j += 1
        if (a % i == 0) and (b % i == 0):
            print(i, j)
            break


gcd(a, b)


def gcd2(a, b):
    i = 0
    while b > 0:
        r = a % b
        a, b = b, r
        i += 1
    return a, i


print(gcd2(a, b))

print(gcd2(270, 192))
