def compar():
    test = False
    contor = 0
    numar = input('numar =')
    numar_anterior = 0
    while numar != 0:
        if numar > numar_anterior:
            if not test:
                test = True
            elif test:
                contor += 1
                test = False
        else:
            test = True 
        numar_anterior = numar
        numar = input('numar =')
    print('exista', contor, 'numere mai mari decat vecinii lor in sir')


compar()