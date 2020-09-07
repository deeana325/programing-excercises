# 6. Write a Python program to print a long text, convert the string to a list
#  and print all the words and their frequencies.

text = "jadjd  adjwgskagd aj adjwgskagd ldj  adjwgskagd l lws lws adjwgskagd adjwgskagd lws v jadjd jadjd lws lws jadjd  adjwgskagd aj adjwgskagd ldj  adjwgskagd l lws lws adjwgskagd adjwgskagd lws v jadjd jadjd lws lws jadjd  adjwgskagd aj adjwgskagd ldj  adjwgskagd l lws lws adjwgskagd adjwgskagd lws v jadjd jadjd lws lws "
list = text.split(" ")
for i in set(list):
    count = 0
    for j in list:
        if i == j:
            count += 1
    if i != "":
        print(i, ": ", count)
