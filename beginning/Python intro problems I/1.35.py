#35. Write a Python program that will return true if the two given integer values are equal 
# or their sum or difference is 5.


a = 4
b = 9

def truth(a, b):
    if a == b or a-b == 5 or b-a == 5 or a+b == 5:
        return True
    else:
        return False

print(truth(a, b))

