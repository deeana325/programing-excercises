# 17. Write a Python program to get all strobogrammatic numbers that are of length n. Go to the editor
# A strobogrammatic number is a number whose numeral is rotationally symmetric, so that it appears
# the same when rotated 180 degrees. In other words, the numeral looks the same right-side up and upside
#  down (e.g., 69, 96, 1001).
# For example,
# Given n = 2, return ["11", "69", "88", "96"].
# Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']
import random


def choice(l):
    """pick a random element from a list"""
    assert len(l) > 0, "Error: choice requires non-empty list"
    return l[random.randint(0, len(l) - 1)]


def all_combinations(n: int, l: list) -> list:
    assert n > 0, "n should be greater than 0"
    if n == 1:
        return l
    prev: list = all_combinations(n - 1, l)
    rez: list = []
    for i in prev:
        for j in l:
            rez.append(i + j)
    return rez


def filter_0(l: list) -> list:
    return [x for x in l if x[0] != "0"]


def flip_str(s: str) -> str:
    mirror = s[::-1]
    mirror = list(mirror)
    for i in range(len(mirror)):
        if mirror[i] == "6":
            mirror[i] = "9"
        elif mirror[i] == "9":
            mirror[i] = "6"
    acc = ""
    for c in mirror:
        acc = acc + c
    print("acc:", acc)
    return acc


def strobo_num(n: int) -> list:
    head = filter_0(all_combinations(n // 2, ["0", "1", "6", "8", "9"]))
    tail = [flip_str(x) for x in head]
    if n % 2 == 0:
        middle = [""]
    else:
        middle = ["0", "1", "8"]
    acc = []
    for i in range(len(head)):
        for m in middle:
            acc.append(head[i] + m + tail[i])
    return acc


print(strobo_num(3))
