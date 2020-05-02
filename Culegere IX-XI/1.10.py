def palindrom(numar):
    return numar == numar[::-1]


x = input("introdu un nr de 4 cifre:")
assert len(x) == 4, "trebuie sa aiba 4 cifre"

try:
    x_int = int(x)
except:
    raise Exception("nu este int")
x = 1

try:
    if palindrom(x):
        print(x, "este un palindrom")
    else:
        print(x, "nu este un palindrom")
except Exception as e:
    raise Exception("nu a mers -" + str(e))
