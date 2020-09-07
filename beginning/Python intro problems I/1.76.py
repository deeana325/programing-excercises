# 76. Write a Python program to get the command-line arguments (name of the script, the number of
# arguments, arguments) passed to a script.

import sys

print('name:', sys.argv[0])
print('number of arguments:', len(sys.argv))
print('list of arguments:', str(sys.argv))

