import re

path = "/Users/diana/Documents/School+/Python/regex/corpus.txt"

# gaseste numere intregi, gaseste numere float, gaseste cuvinte care incep cu majuscula
pattern = ["(?<intregi>(?<![\.0-9])[0-9]+(?![\.0-9]))", "(?<reale>[0-9]+\.[0-9]+)", "(?<cuv_majusc>(?<!\w)[A-Z][a-z]+(?!\w))"]


with open(path, "r") as file:
    for i in range(len(pattern)):
        re.search(pattern[i], file)

print(intregi, "\n", reale, "\n", cuv_majusc)

# nu merge...(da eroare) dar regexurile sunt bune
