# 59. Write a Python program to convert height (in feet and inches) to centimeters.


def inaltime(feet, inches):
    return feet*30.48 + inches*2.54


f = 5
i = 8

print(inaltime(f, i), 'cm')
