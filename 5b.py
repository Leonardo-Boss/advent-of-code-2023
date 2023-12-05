with open("inputs/5", "r") as f:
    data = f.readlines()

with open("tests/5", "r") as f:
    tdata = f.readlines()
data = tdata

seeds = list(map(int,data[0].removeprefix('seeds: ').strip().split()))
seeds = [(seed1,l) for seed1,l in zip(seeds[::2],seeds[1::2])]
seeds

transformations = {}
key = None
for i in data[1:]:
    if i[0].isalpha():
        i = i.removesuffix(' map:\n')
        key = i 
    elif i[0].isdigit():
        i = list(map(int,i.split()))
        i[2] = i[1]+i[2]
        transformations[key] = transformations.get(key, []) + [i]

results = []
for seed in seeds:
    trans = seed
    for key, transformation in transformations.items():
        for destiny, start, end in transformation:
            if trans < start or trans >= end: continue
            trans = trans-start+destiny
            break
    results.append(trans)
print(min(results))
