#40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

a = (3, 5)
b = (7, 3)

def distance(a, b):
    x1, y1 = a
    x2, y2  = b
    return sqrt((x1 - x2)^2 + (y1 - y2)^2)

print (distance(a, b))