def shuuffle_1(l: list) -> list:
    import random

    n = len(l)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i + 1)
        l[i], l[j] = l[j], l[i]
    return l


l = [1, 2, 3, 4, 5, 6]
print(shuuffle_1(l))
