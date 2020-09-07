#56. Write a Python program to get height and width of the console window.

import os

columns, rows = os.get_terminal_size(0)

print('width:', columns, 'length:', rows)