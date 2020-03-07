# 1. Write a Python function that takes a sequence of numbers and determines whether all the 
# numbers are different from each other.

def test(list):
    for i in list:
        contor = 0
        for j in list:
            if i == j:
                if  contor == 0:
                    contor = contor + 1    
                else: 
                    return False
    return True

list = [1, 2, 5, 5, 3]
print(test(list))



