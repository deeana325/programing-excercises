# 3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.


l = [3, 56, 2, 63, 1, 46, 143, 65124, 412]


def remove_print_3(l, n):
    for i in l:
        if sum(l) == 0:
            print('Lista este goala!')
            print(l)
        else:
            if n >= len(l):
                l[n] = 0
                remove_print_3(l, len(l) - n + 2)
            else:
                l[n] = 0
                remove_print_3(l, n + 3)


def remove_print_3_v2(l, k=3):
    poz = 0
    while len(l) > 0:
        print(l.pop(poz))
        if len(l) == 0:
            break
        poz = (poz + k - 1) % len(l)


remove_print_3_v2(l)
