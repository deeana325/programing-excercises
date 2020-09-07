# 73. Write a Python program to calculate midpoints of a line.


def midpoint(x, y: tuple):
    x1, x2 = x
    y1, y2 = y
    return (x1+y1)/2, (x2+y2)/2


m = midpoint((7, -2), (2, 5))
print(m)
