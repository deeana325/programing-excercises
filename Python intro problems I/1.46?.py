#46. Write a python program to get the path and name of the file that is currently executing.
import os
print(os.path.dirname(sys.argv[0]))