l = [1, 2, [3, 4], [[5]]]

def list_depth(l):
    if type(l) != list:
        return 0
    else:
        depths = []
        for x in l:
            depths.append(list_depth(x))
        return 1 + max(depths)


print(list_depth(l))
