#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import os, glob, sys

pattern = sys.argv[1]

lista_fisiere = glob.glob(pattern)

for x in lista_fisiere:
    if os.path.isfile(x):
        print(x, ' '*(32 - len(x)), os.path.getsize(x), 'Bytes')

print('total:', sum(os.path.getsize(x) for x in lista_fisiere if os.path.isfile(x)), 'Bytes')    
