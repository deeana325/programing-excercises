def insertion_sort(l: list):
    l = [] + l
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j = j - 1
    return l


assert insertion_sort([1, 0, 4]) == [0, 1, 4]
assert insertion_sort([]) == []
assert insertion_sort([4]) == [4]
assert insertion_sort([2, 2, 2]) == [2, 2, 2]
assert insertion_sort([3, 2, 1]) == [1, 2, 3]


def timer(function, arg):
    import time

    t0 = time.time()
    rez = function(arg)
    dt = time.time() - t0
    print("time=", round(dt, 3))
    return rez


# !!!!!  pot sa fac cumva sa nu mai calculeze functia de cand i-o dau ci sa o calculeze cand i-o atribui lui rez?   !!!!!

import random

test_list = [random.randint(0, 1000) for i in range(10000)]

timer(insertion_sort, test_list)


# test_list = [random.randint(0, 1000) for i in range(1000)]

# t0 = time.time()
# # test_list = [2, 7, 3, 4, 1, 6, 5, 8]
# rez = sorted(test_list)
# # print(rez)
# dt = time.time() - t0
# print("time=", round(dt, 3))
