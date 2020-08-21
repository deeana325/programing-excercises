def merge_sort(l: list, low, high):
    if len(l[low:high]) == 1:
        return
    else:
        merge_sort(l, low, high // 2)
        merge_sort(l, high // 2 + 1, high)
    merge(l, low, high // 2, high)


def merge(l: list, low: int, middle: int, high: int):
    i = low
    j = middle
    rez = []

    if l == []:
        return l
    should_continue = False
    while i < middle or j <= high:
        if should_continue:
            break
        if l[i] <= l[j] and i < middle:
            rez.append(l[i])
            if i < middle - 1:
                i += 1
            elif i >= middle - 1:
                should_continue = True
        if l[i] >= l[j] and j <= high:
            rez.append(l[j])
            if j < high:
                j += 1
            elif j >= high:
                should_continue = True
    while i < middle and l[i] > rez[-1]:
        rez.append(l[i])
        i += 1
    while j < high and l[j] > rez[-1]:
        rez.append(l[j])
        j += 1
    if high != len(l) - 1:
        return l[:low] + rez + l[high + 1 :]
    else:
        return l[:low] + rez


# def merge_2(l1: list, l2: list) -> list:
#     rez = []
#     while True:
#         if len(l1) == 0:
#             rez += l2
#             break
#         elif len(l2) == 0:
#             rez += l1
#             break
#         elif l1[0] < l2[0]:
#             rez.append(l1.pop(0))
#         else:
#             rez.append(l2.pop(0))
#     return rez


# def test_merge_2():
#     assert merge_2([], []) == []
#     assert merge_2([1, 4], [2, 3]) == [1, 2, 3]
#     assert merge_2([1, 5, 7, 9], [0]) == [0, 1, 4, 5, 7, 9]
#     assert merge_2([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge():
    assert merge([], 0, 0, 0) == []
    assert merge([1, 4, 2, 3], 0, 2, 3) == [1, 2, 3, 4]
    assert merge([1, 5, 7, 0, 4, 9], 0, 3, 5) == [0, 1, 4, 5, 7, 9]
    assert merge([1, 3, 5, 2, 4], 0, 3, 4) == [1, 2, 3, 4, 5]
    assert merge([1, 1, 2, 5, 0, 0, 5, 5, 5], 0, 4, 8) == [0, 0, 1, 1, 2, 5, 5, 5, 5]


test_merge()

# assert merge_sort([1, 0, 4], 0, 3) == [0, 1, 4]
# assert merge_sort([], 0, 1) == []
# assert merge_sort([4], 0, 1) == [4]
# assert merge_sort([2, 2, 2], 0, 3) == [2, 2, 2]


# test_list = [2, 7, 3, 4, 1, 6, 5, 8]
# merge_sort(test_list, 0, len(test_list))
# print(test_list)
