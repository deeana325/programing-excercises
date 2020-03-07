import sys

nr = 0
for line in sys.stdin:
    print(line.upper(), end='')
    nr += 1
    if nr % 10 == 0:
        print(nr, file=sys.stderr)


    
    