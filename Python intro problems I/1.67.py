# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch,
#  a millimeter of mercury (mmHg) and atmosphere pressure.


def psi_mmHg_atm(kPa):
    return kPa/6.895, kPa/7.501, kPa/101


x = psi_mmHg_atm(1002)
psi, mmHg, atm = x
print(psi, 'pounds per square inch')
print(mmHg, 'milimeters of mercury')
print(atm, 'atmosphere preassure')
