def binary_search(l: list, x: int, low=0, high=None):
    if not l:
        return None
    if high is None:
        high = len(l) - 1
    # print("interval=", high - low)
    if x < l[low] or x > l[high]:
        return None
    pivot = (low + high) // 2
    if x == l[pivot]:
        return pivot
    elif x < l[pivot]:
        return binary_search(l, x, low, pivot - 1)
    elif x > l[pivot]:
        return binary_search(l, x, pivot + 1, high)


assert binary_search([], 0) == None
assert binary_search([4], 4) == 0
assert binary_search([1, 2, 3], 4) == None
assert binary_search([2, 2, 2], 2) == 1
assert binary_search([1, 2, 3, 5, 7, 8, 9], 7) == 4
assert binary_search(list(range(1024)), 1) == 1

# l = [5, 2, 3, 1, 4]
# l.sort()

# print(l[binary_search(4, l)])

