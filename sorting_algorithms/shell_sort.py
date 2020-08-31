def insertion_sort(l: list):
    l = [] + l
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j = j - 1
    return l


def shell_sort(l: list, gap=None, i=0) -> list:
    if l == []:
        return l
    if gap is None:
        gap = len(l) // 2
    if gap == 1:
        return insertion_sort(l)
    else:
        x = i + gap
        while i < x:
            j = i
            temp_l = []
            while j <= len(l) - 1:
                temp_l.append(l[j])
                j += gap
            temp_l = insertion_sort(temp_l)
            j = i
            k = 0
            while j <= len(l) - 1:
                l[j] = temp_l[k]
                k += 1
                j += gap
            i += 1
    return shell_sort(l, gap // 2)


assert shell_sort([]) == []
assert shell_sort([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
assert shell_sort([8, 3, 5, 9, 2, 0, 1]) == [0, 1, 2, 3, 5, 8, 9]
assert shell_sort([4, 0, 1, 5, 3, 8, 7, 9, 2, 6]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert shell_sort([1, 1, 0, 3, 2, 2, 3, 0, 4, 7, 4]) == [
    0,
    0,
    1,
    1,
    2,
    2,
    3,
    3,
    4,
    4,
    7,
]

