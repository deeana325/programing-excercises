import sys


src_fname = 'lectia3.py'
dest_fname = 'o2'
with open(src_fname, 'r') as f:
    with open(dest_fname, 'w') as f2:
        nr = 0
        for line in f:
            print(line.upper(), file=f2,  end='')
            nr += 1
            if nr % 10 == 0:
                print(nr, file=sys.stderr)


    
    