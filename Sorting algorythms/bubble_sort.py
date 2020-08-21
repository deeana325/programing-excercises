def bubble_sort(l: list):
    l = [] + l
    needs_order = True
    while needs_order:
        needs_order = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                needs_order = True
    return l


assert bubble_sort([1, 0, 4]) == [0, 1, 4]
assert bubble_sort([]) == []
assert bubble_sort([4]) == [4]
assert bubble_sort([2, 2, 2]) == [2, 2, 2]


l = [1, 6, 2, 5, 8, 3, 5, 6, 9, 3]
print(bubble_sort(l))

# Tema: insertion sort
# merge sort
# sa masor cat dureaza executia lui bubblesort pe o lista de 1k, 10k, 100k, 1M  (random.shuffle - ca sa amestec lista generata de range)
