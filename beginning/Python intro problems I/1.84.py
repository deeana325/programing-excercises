# 84. Write a Python program to count the number occurrence of a specific character in a string.


def count_occurance(string, character):
    contor = 0
    for i in string:
        if character == i :
            contor += 1
    return contor

print('Caracterul "a" se gaseste de', count_occurance('ana are mere rosii', 'a'), 'in propozitia "Ana are mere"')                
