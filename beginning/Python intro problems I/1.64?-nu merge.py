# 64. Write a Python program to get file creation and modification date/times.

import os
import time

print('created: %s' % time.ctime(os.path.getctime('1.63.py')))
print('last modified: %s' % time.ctime(os.path.getmtime('1.63.py')))
