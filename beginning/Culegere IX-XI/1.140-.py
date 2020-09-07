import sys


def suma(n: int) -> list:
    # write n as a sum of consecutive integers
    rez = []
    for i in range(1, n):
        for j in range(i + 1, n):
            sum_i_to_j = (i + j) * (j - i + 1) // 2
            if sum_i_to_j == n:
                rez.append(list(range(i, j + 1)))
    return rez


if suma(5) != [[2, 3]]:
    print("Error")
    sys.exit()
assert suma(50) == [[8, 9, 10, 11, 12], [11, 12, 13, 14]], "Wrong result"
print(suma(20))
