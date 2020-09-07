# 90. Write a Python program to create a copy of its own source code.
import os, shutil


source = '/Python/1.90.py'
destination = '/Python'
shutil.copy2(source, destination)
