#51. Write a Python program to determine profiling of Python programs.


import os, glob, cProfile

def lista():
    terminatiaTipuluiDeFisier = 'py'

    listaFisiere = glob.glob('*.' + terminatiaTipuluiDeFisier)

    for x in listaFisiere:
        if os.path.isfile(x):
            print(x, ' '*(32 - len(x)), os.path.getsize(x), 'Bytes')

    print('total:', sum(os.path.getsize(x) for x in listaFisiere if os.path.isfile(x)), 'Bytes')    


cProfile.run('lista()')