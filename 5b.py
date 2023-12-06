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

transformations = list(transformations.items())

transformers = []
def get_transf(tranformations):
    if len(transformations) == 1:
        pass
    t = []
    for destiny1, start1, end1 in transformations[0]:
        for destiny2, start2, end2 in transformations[1]:
            array = ((start1, destiny1, True),
                    (start2, destiny2, True),
                    (end1, destiny1, False),
                    (end2, destiny2, False),)
            s = sorted(array, key=lambda x: x[0])

            # startsmall - start bigger/ endsmall
            ds = start1 - start2
            de = end2 - end1
            if start1 >= start2 and end1 < end2:
                t.append(destiny1-start2+destiny2)


for destiny, start, end in first:
    for key, transformation in transformations:
        for destiny, start, end in transformation:
            if trans < start or trans >= end: continue
            trans = trans-start+destiny
            break
print(min(results))
