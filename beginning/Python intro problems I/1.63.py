# 63. Write a Python program to get an absolute file path.
import os, glob

# print(os.path.abspath('1.63.py'))

# full_path = os.path.abspath('1.63.py')

# print(os.path.basename(full_path))

# print(os.path.dirname(full_path))

# print(os.path.join('/Users/diana/Desktop', 'cucu', 'bau.py'))

# print('getcwd = ', os.getcwd())

for fname in glob.glob('../../Downloads/*.jpg'):
    tip = 'file'
    if os.path.isdir(fname):
        tip = 'dir '
    print(tip, fname)