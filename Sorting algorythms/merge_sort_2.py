def merge_sort(l: list) -> list:
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    l1 = merge_sort(l[:mid])
    l2 = merge_sort(l[mid:])
    return merge(l1, l2)


def merge(l1: list, l2: list) -> list:
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    rez = []
    c1 = 0
    c2 = 0
    while c1 < len(l1) or c2 < len(l2):
        if c1 == len(l1):
            rez += l2[c2:]
            break
        if c2 == len(l2):
            rez += l1[c1:]
            break
        if l1[c1] < l2[c2]:
            rez.append(l1[c1])
            c1 += 1
        else:
            rez.append(l2[c2])
            c2 += 1
    return rez


def test_merge():
    assert merge([], []) == []
    assert merge([], [1, 3]) == [1, 3]
    assert merge([1, 3], []) == [1, 3]
    assert merge([1, 2, 7], [0, 3, 4, 5, 6]) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert merge([1, 1, 2, 5], [0, 0, 5, 5, 5]) == [0, 0, 1, 1, 2, 5, 5, 5, 5]


test_merge()


def test_merge_sort():
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([1, 2, 3]) == [1, 2, 3]
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([1, 4, 2, 5, 3, 0]) == [0, 1, 2, 3, 4, 5]
    assert merge_sort([1, 1, 0, 3, 5, 0, 2, 3, 2]) == [0, 0, 1, 1, 2, 2, 3, 3, 5]


test_merge_sort()

