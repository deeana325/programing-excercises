#7. Write a Python program to count the number of each character of a given text of a text file.
v = []
for i in range(0, 255):
    v[i] = 0

def char_count(nume_fisier):
    with open(nume_fisier, 'r') as f:
        while True:
            c = f.read(1)
            if not c:
                break    
            v[ord(c)] += 1 
    for i in (0,32):
        v[i] = 0
    print('In fisier exista urmatoarele caractere:')    
    for i in range(0, 255):
        if v[i] != 0:
            print(chr(i), ':', v[i])


char_count('/Users/diana/Documents/School+/Python/Python intro problems II/data.txt')           

