# 17. Write a Python program to get all strobogrammatic numbers that are of length n. Go to the editor
# A strobogrammatic number is a number whose numeral is rotationally symmetric, so that it appears 
# the same when rotated 180 degrees. In other words, the numeral looks the same right-side up and upside
#  down (e.g., 69, 96, 1001).
# For example,
# Given n = 2, return ["11", "69", "88", "96"].
# Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']


def strobogrammatic_or_not(x):
    vect_x = list(str(x))
    if len(vect_x) % 2 == 0:
        
    
    else:
