n_samples = 1000
seed = 1234
counter = []
for i in range(100):
    counter.append(0)


for i in range(100 * n_samples):
    seed = (seed * 126341731 + 10238187) % 4872916371
    # print(seed % 100, seed)
    counter[seed % 100] += 1

counter = [round(x / n_samples, 3) for x in counter]
print(counter)

