l = [1, 5, 2, 3]

def rec_max(l):
    if len(l) == 1:
        return l[0]
    else:
        mr = rec_max(l[1:])
        if l[0] > mr:
            return l[0]
        else:
            return mr

print(rec_max(l))
