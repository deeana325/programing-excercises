print('str= ')
s= str(input())
l= ['a','e','i','o','u']
x=0
for i in range(0,len(s)):
    if s[i] in l:
        x+=1
print(x)

# for i in range(1,21):
#     for j in range(1,21):
#         for g in range(1,21):
#             print(i,'*',j,'*',g,'= ',i*j*g)
