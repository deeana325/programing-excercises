#50. Write a Python program to print without newline or space.

a = '50. Write a Python program to print without newline or space.'

def printInLine(a):
    s = a.split(' ')
    for i in s:
        print(i, end='')
    print('')    

printInLine(a)        


