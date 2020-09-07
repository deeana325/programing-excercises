#37. Write a Python program to display your details like name, age, address in three different lines.

name = 'addf'
age = 3
address = 'fdsd'

def info(name, age, address):
    print('\n', name , '\n', age, '\n', address)

def info2(*args):
    for x in args:
        print(x)


info2(name, age, address, address)


print()