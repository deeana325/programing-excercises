
a = [1, 2, 3]
b = []
c = []
turnuri = [a, b, c]


def hanoi(n, origine, destinatie):
    if n > 1:
        for rezerva in turnuri:
            if rezerva not in [origine, destinatie]:
                hanoi(n - 1, origine, rezerva)
        else:
            if n==1:
                destinatie.append(origine.pop(len(origine)))
                print(a, b, c)
        
        destinatie.append(origine.pop(len(origine)))
        print(a, b, c)
        for rezerva in turnuri:
            if rezerva not in [origine, destinatie]:
                hanoi(n - 1, rezerva, destinatie)

hanoi(len(a), a, c)            