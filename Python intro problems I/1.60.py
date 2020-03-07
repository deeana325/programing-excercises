# 60. Write a Python program to calculate the hypotenuse of a right angled triangle.
import math


def ipotenuza(a, b):
    return math.sqrt(a**2 + b**2)


a = 4
b = 3

print(ipotenuza(a, b))
