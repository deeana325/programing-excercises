# read eval print loop

while True:
    cmd = input('> ')
    rez = eval(cmd, globals(), locals())
    print(str(rez))
