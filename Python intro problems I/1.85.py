# 85. Write a Python program to check whether a file path is a file or a directory. 

import os

def isfile(path):
    if os.path.isdir(path):
        return 'directory'
    else:
        return 'file'    


print('The path leads to a', isfile('/Desktop/Python/1.50.py'))




