# 78. Write a Python program to find the available built-in modules.

import pip, subprocess, sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])