# 26. Write a Python program to create a histogram from a given list of integers.

def histogram(l):
    for x in l:
        if x < 10:
            print(x, end = '  ')
        else:
            print(x, end = ' ')    
        print(x*'@')


histogram([1, 5, 3, 20, 8, 5])        
