#15. Write a Python program to check the priority of the four operators (+, -, *, /).

operators = {
    '+' : '0',
    '-' : '0',
    '*' : '1',
    '/' : '1',
}

def priority(o1, o2):
    return operators[o1] >= operators[o2]

o1 = input('operator 1:')
o2 = input('operator 2:')

if priority(o1, o2) and priority(o2, o1):
    print(o1, 'and', o2, 'have the same priority.')
else:
    if priority(o1, o2):
        print(o1, 'has a higher priority than', o2, '.')
    else:
        if priority(o2, o1):
            print(o1, 'has a lower priority than', o2, '.')    