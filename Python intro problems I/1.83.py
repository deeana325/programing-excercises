# 83. Write a Python program to test whether all numbers of a list is greater than a certain number.

number = 4
list = [8, 398, 38, 21, -56]
truth = True
for i in list:
    if i <= number:
        truth = False

if truth:
    print('Toate numerele sunt mai mari decat', number)
else:
    print('Exista cel putin un numar mai mic decat', number)

