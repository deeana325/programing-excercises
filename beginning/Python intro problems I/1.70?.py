# 70. Write a Python program to sort files by date.
import os


fisiere = filter(os.path.isfile, os.listdir('diana/Desktop/Python'))
sorted(fisiere, key=os.path.getmtime)
for i in fisiere:
    print(i)