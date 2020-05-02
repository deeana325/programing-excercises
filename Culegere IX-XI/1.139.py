import readchar


def compar():
    test = True
    contor = 0
    numar = input('numar = ')
    numar_anterior = '0'
    while numar != '0':
        if test and numar > numar_anterior:
                contor += 1
                test = False
        elif numar < numar_anterior:
            test = True 
        numar_anterior = numar
        numar = input('numar = ')
    print('exista', contor, 'numere mai mari decat vecinii lor in sir')

# ch = ''
# while ch != '0':
#     ch = readchar.readchar()
#     print(ord(ch), ch)


compar()