

def hanoi_complexity(n_max):
    a = list(range(n_max, 0, -1))
    b = []
    c = []
    nr = 0

    def hanoi(n, origine, rezerva, destinatie):
        # print(a, b, c)
        nonlocal nr
        nr += 1
        if n > 1:
            hanoi(n - 1, origine, destinatie, rezerva)
        if n >= 1:    
            destinatie.append(origine.pop())
        if n > 1:
            hanoi(n-1, rezerva, origine, destinatie)

    hanoi(len(a), a, b, c)
    # print(a, b, c)
    return nr


comp = [1]
for level in range(3, 31):
    comp.append(hanoi_complexity(level))
    print(level, comp[-1], comp[-1]/comp[-2])            