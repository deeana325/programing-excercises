# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of
# a given string. Return the n copies of the whole string if the length is less than 2.

# def solutie(s, n):
#     if len(s) < 2:
#         return s*n
#     else:
#         return s[:2]*n

def solutie2(s, n):
    return s[:2]*n        

print(solutie2('abc3', 3))
print(solutie2('a', 5))
print(solutie2('', 10))
