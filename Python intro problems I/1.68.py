# 68. Write a Python program to calculate the sum of the digits in an integer.


def sum_of_digits(x):
    y = 0
    for i in str(x):
        y = y+int(i)
    return y


print(sum_of_digits(4747))
