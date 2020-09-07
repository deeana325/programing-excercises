x=float(input('number: '))
r=1000
for i in range(0,2):
    if x<=(r+100) and x>=(r-100):
        print('the number is within 100 of', r)
    r=r+1000    
