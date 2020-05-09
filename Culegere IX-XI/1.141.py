#   Pentru inmultirea A = {1, 2, 3, ..., m} si B = {1, 2, ..., n} 
# sa se afiseze elementele multimii AxB = { (a,b) |a ∈ A, b ∈ B}.

m = int(input("m = "))
n = int(input("n = "))
AxB = []

for i in range(1,m+1):
    for j in range(1,n+1):
        AxB.append((i, j))

print("AxB =", AxB)
