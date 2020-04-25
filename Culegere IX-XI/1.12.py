

def test_patrat_perfect(numar):
    i = 1
    while i**2 <= numar:
        if i**2 == numar:
            return True
        i += 1
    return False


x = 123201 
if test_patrat_perfect(x):
    print(x, 'este patrat perfect')
else:
    print(x, 'nu este patrat perfect')            