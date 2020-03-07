#7. Write a Python program to count the number of each character of a given text of a text file.


def char_count(nume_fisier, pozitie_init, pozitie_fin):
    f = open(nume_fisier, 'r')
    count = 0
    seek = pozitie_init
    while seek <= pozitie_fin:
        if f.read() in 'abcdefghijklmnopqrstuvwxyz':
            count +=1
        seek +=1
    return count        

