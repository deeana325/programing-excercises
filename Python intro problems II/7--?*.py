# 7. Write a Python program to count the number of each character of a given text of a text file.
import traceback

v = [0] * 256


def inc_chr(c):
    global v
    v[ord(c)] += 1


def char_count(nume_fisier):

    global v
    with open(nume_fisier, "r") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            try:
                inc_chr(c)
            except Exception as e:
                # print(traceback.format_exc())
                print("Crapa", str(e), ord(c), c)

    print("In fisier exista urmatoarele caractere:")
    for i in range(0, 255):
        if v[i] != 0:
            ch = chr(i) if i >= 32 else " "
            print(ch, ":", v[i])


char_count("/Users/diana/Documents/School+/Python/Python intro problems II/data.txt")
