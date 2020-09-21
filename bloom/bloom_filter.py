import os
import hashlib
import re

data_path = "/Users/diana/Documents/School+/Python/bloom"
src_file = os.path.join(data_path, "corpus.txt")
dest_file = os.path.join(data_path, "dictionary_corpus.txt")
bloom = [0] * 1000000


def hash_str(s, max_value=1000000):
    h = int(hashlib.md5(s.encode()).hexdigest(), 16)
    return h % max_value


def log_str(s):
    bloom[hash_str(s)] += 1


def check_str(s):
    return bloom[hash_str(s)]


# !!!!!!!!!!!!!!!!!!! 


def tokenize(s):
    return [re.sub(r"([,;:\.()_]+|^[\W_]*|[\W_]*$)", "", x) for x in re.split(r'(!| )+', re.sub(r'^[ \s]*|[ \s]*$', '', s.lower()))]
    # return [re.sub(r'[,;:\/.()]+', '', x) for x in s.lower().strip().split()]


with open(dest_file, "w") as file2:
    with open(src_file, "r") as file1:
        for line in file1:
            for word in tokenize(line):
                if check_str(word) == 0:
                    log_str(word)
                    file2.write(word + "\n")
                    # print(word, file=file2)
