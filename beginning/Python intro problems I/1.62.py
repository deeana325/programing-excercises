# 62. Write a Python program to convert all units of time into seconds.


def secunde_totale(zile, ore, minute, secunde):
    return zile*24*3600 + ore*3600 + minute*60 + secunde


zile = 3
ore = 7
minute = 5
secunde = 57

print(secunde_totale(zile, ore, minute, secunde), 'secunde')
