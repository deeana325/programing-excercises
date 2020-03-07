# 65. Write a Python program to convert seconds to day, hour, minutes and seconds.


def zile_ore_minute_secunde(secunde):
    zile = secunde//(24*3600)
    secunde = secunde % (24*3600)
    ore = secunde//3600
    secunde = secunde % 3600
    minute = secunde//60
    secunde = secunde % 60
    return zile, ore, minute, secunde

print(zile_ore_minute_secunde(284757))