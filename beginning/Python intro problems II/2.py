# 2. Write a Python program to create all possible strings by using
# 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

# def all_variants(l1, contoar):
#     for i in l1:
#         if contoar == len(l1):
#             all_variants[x] = sum[variant]
#         else: if i != z for z in variant:
#             variant[y] = i

letters = ["a", "e", "i", "o", "u"]


def solution1(letters):
    n = 0
    for l1 in letters:
        for l2 in letters:
            if l2 != l1:
                for l3 in letters:
                    if l3 not in [l1, l2]:
                        for l4 in letters:
                            if l4 not in [l1, l2, l3]:
                                for l5 in letters:
                                    if l5 not in [l1, l2, l3, l4]:
                                        n += 1
                                        print(n, l1 + l2 + l3 + l4 + l5)


def solution2(part, n):
    if len(letters) == len(part):
        n += 1
        print(n, part)
    else:
        for l in letters:
            if l not in part:
                n = solution2(part + l, n)
    return n


solution2("", 0)
