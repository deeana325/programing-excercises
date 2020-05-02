def test_patrat_perfect(numar):
    return int(x ** 0.5) ** 2 == x


x = 123201
if test_patrat_perfect(x):
    print(x, "este patrat perfect")
else:
    print(x, "nu este patrat perfect")
