#36. Write a Python program to add two objects if both objects are an integer type.

a = int(3)
b = float(4)

def add_numbers(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError("Inputs must be integers")
    return a + b

print(add_numbers(a, b))
