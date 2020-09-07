# 77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.

import sys 

if sys.byteorder == 'little':
    print('The system is a little-endian platform')
else:
    print('The system is a big-endian platform') 
