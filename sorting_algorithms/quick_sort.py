def quick_sort(l: list, pivot=None, contor=0):
    if pivot is None:
        pivot = len(l) - 1
    if l == [] or len(l) == 1:
        return l
    beginning = contor
    switch = contor
    if len(l[contor : pivot + 1]) < 2:
        return
    while contor <= pivot - 1:
        if l[contor] <= l[pivot]:
            if contor != switch:
                l[contor], l[switch] = l[switch], l[contor]
            contor += 1
            switch += 1
        elif l[contor] > l[pivot]:
            contor += 1
    if l[switch] > l[pivot]:
        l[switch], l[pivot] = l[pivot], l[switch]
    quick_sort(l, switch - 1, beginning)
    if switch < len(l) - 1:
        quick_sort(l, pivot, switch + 1)
    return l


assert quick_sort([1, 0, 4]) == [0, 1, 4]
assert quick_sort([]) == []
assert quick_sort([4]) == [4]
assert quick_sort([2, 2, 2]) == [2, 2, 2]


l = [2, 5, 4, 0, 1, 3]
print(quick_sort(l, len(l) - 1))


def timer(function, arg):
    import time

    t0 = time.time()
    rez = function(arg)
    dt = time.time() - t0
    print("time=", round(dt, 3))
    return rez


import random

test_list = [random.randint(0, 1000) for i in range(10000)]

timer(quick_sort, test_list)

