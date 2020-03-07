# Write a program that will accept a path and list the files like ls.

import glob, sys, os

def myls(path):
    print('\n'.join(glob.glob(path)))

# print('\n'.join(glob.glob('../Books/*.pdf')))
if len(sys.argv) > 1:
    myls(sys.argv[1])
    # print()
    # print(sys.argv)
else:
    # myls(os.getcwd() + '/*')    
    myls('../'*2 + '*')    

'''

# ls | cut -c 1,2 | sort | uniq -c | sort -n -r

x = ls
x = cut -c 1,2 (x)
x = sort (x) 
x = uniq -c (x)
x = sort -n -t (x)
print(x)

'''