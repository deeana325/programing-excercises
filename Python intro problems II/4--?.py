# 4. Write a Python program to find unique triplets whose three elements gives the
#  sum of zero from an array of n integers.

# sample = [1, -1, 5, 3, 0, 83, -83, 2, -5, 4, 52, 1, 35, 4, 4, -8]
sample = [1, -1, 0, 1]


# def triplets_sum_0(solution:list, triplet:tuple, i):
#     if len(triplet) = 1 and i = len(sample) - 1:
#         print(solution)
#     if len(triplet) < 3 and i >= len(sample):  #poate ajunge si i = len(sample) dar ca sa fiu sigura am pus >=
#         break
#     if len(triplet) == 3:
#         if sum(triplet) == 0 and triplet not in solution:
#             return solution + triplet #nu sunt sigura daca asta o sa faca solutia sa fie retinuta
#         else:
#             break 
#     else:
#         for n in sample[i:]:
#             triplets_sum_0(solution, triplet + n, i + #pozitia lui n in sample(nu stiu cum sa scriu asta) + 1)

def triplets_sum_0(triplet):
    if len(triplet) == 3:
        if sample[triplet[0]] + sample[triplet[1]] + sample[triplet[2]] == 0:
            return [triplet]
        else:
            return []
    else:
        rez = []
        for i in range(len(sample)):
            if len(triplet) > 0 and i <= max(triplet): continue
            rez += triplets_sum_0(triplet + [i])
        return rez


print(triplets_sum_0([]))



