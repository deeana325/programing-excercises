#Write a Python program to compute the future value of a specified 
# principal amount, rate of interest, and a number of years.

x = 10000
n = 1000000
p = 5/n/100

for i in range(n):
    dob = x * p
    x = x + dob

print(x)

