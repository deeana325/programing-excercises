# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.


def inches_yards_miles(feet):
    return feet*12, feet/3, feet/5280


r = inches_yards_miles(528)

print(r)
