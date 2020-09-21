import os
import hashlib
import re
import math

data_path = "/Users/diana/Documents/School+/Python/bloom"
src_file = os.path.join(data_path, "corpus.txt")
unigram = {}
trigram = {}


def tokenize(s):
    return [re.sub(r"([,;:\.()_]+|^[\W_]*|[\W_]*$)", "", x) for x in re.split(r"(!| )+", re.sub(r"^[ \s]*|[ \s]*$", "", s.lower()))]
    # return [re.sub(r'[,;:\/.()]+', '', x) for x in s.lower().strip().split()]


with open(src_file, "r") as file1:
    for line in file1:
        line_tok = tokenize(line.strip())
        line_tok = [x for x in line_tok if x]
        for word in line_tok:
            if word in unigram:
                unigram[word] += 1
            else:
                unigram[word] = 1
            # unigram[word] = unigram.get(word, 0) + 1 -> unigram.get se uita si da valoarea chiar daca nu e in dictionar, daca nu e da none, dar daca are ', 0' da 0
        for word1, word2, word3 in zip(line_tok[:-2], line_tok[1:-1], line_tok[2:]):
            word123 = word1 + " " + word2 + ' ' + word3
            trigram[word123] = trigram.get(word123, 0) + 1

rez = []
for word123 in trigram:
    word1, word2, word3 = word123.split()
    pmi = math.log(len(trigram) ** 2.5 * trigram[word123] ** 0.5 / (unigram[word1] * unigram[word2] * unigram[word3]))
    if trigram[word123] > 15:
        rez.append((word123, pmi))
rez = sorted(rez, key=lambda x: -x[1])

for word, pmi in rez[:100]:
    print(f'{round(pmi, 2):8} | {word}')

i = 0
