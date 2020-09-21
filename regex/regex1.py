import re

path = "/Users/diana/Documents/School+/Python/regex/corpus.txt"

# gaseste numere fractionare, gaseste numere intregi, gaseste cuvinte care incep cu majuscula
p1 = re.compile(r"([0-9]+\.[0-9]+)")
p2 = re.compile(r'((?<![\.0-9])[0-9]+(?![\.0-9]))')
p3 = re.compile(r"((?<!\w)[A-Z][a-z]+(?!\w))")
s = '1, 2, 3, 4 2.03, 1.74, 0.93 Ana are mere. Pe fica morarului o cheama Ana.'
g1, g2, g3 = [], [], []

with open(path, "r") as file:
    for line in file:
        g1 += p1.findall(line.strip())
        g2 += p2.findall(line.strip())
        g3 += p3.findall(line.strip())


print('nr. fractionare:', g1, '\n', 'nr. intregi:', g2, '\n', 'cuv. cu majuscula:', g3)
