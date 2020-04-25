

def palindrom(numar):
    if len(numar) == 4:
        if numar[0] == numar[3] and numar[1] == numar[2]:
            return True
        else:
            return False     
    else:
        print('Error: number not 4 digits') 

x = '1221'               

if palindrom(x):
    print(x, 'este un palindrom')
else:
    print(x, 'nu este un palindrom')    
