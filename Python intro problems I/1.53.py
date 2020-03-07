#53. Write a python program to access environment variables.

import os

import json

print(json.dumps(dict(os.environ), indent=3))