import os
import hashlib
import re
import math

data_path = "/Users/diana/Documents/School+/Python/bloom"
src_file = os.path.join(data_path, "corpus.txt")
unigram = {}
bigram = {}


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
        for word1, word2 in zip(line_tok[:-1], line_tok[1:]):
            word12 = word1 + ' ' + word2
            bigram[word12] = bigram.get(word12, 0) + 1

rez = []
for word12 in bigram:
    word1, word2 = word12.split()
    pmi = math.log(len(bigram) * bigram[word12]**1.5 / (unigram[word1] * unigram[word2]))
    if bigram[word12] > 10:
        rez.append((word12, pmi))
rez = sorted(rez, key = lambda x: -x[1])
i = 0
