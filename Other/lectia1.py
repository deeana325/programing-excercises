

# for i in range(100):
#     if i%2==1:
#         print(i)


for i in range(2,100):
    prim=True
    for j in range(2,i//2):
        if i%j==0:
            prim=False
    if prim:
        print(i)



