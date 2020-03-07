#44. Write a Python program to locate Python site-packages.

import site

print(site.getsitepackages(
    'https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory'))