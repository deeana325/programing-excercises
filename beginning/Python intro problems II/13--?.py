#13. Write a Python program to get all possible two digit letter combinations from a digit (1 to 9) string.

string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}


def combinations():
    for i in range(1,9):
        if string_maps[i]
