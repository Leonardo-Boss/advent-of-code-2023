with open("inputs/5", "r") as f:
    data = f.readlines()

with open("tests/5", "r") as f:
    tdata = f.readlines()
data = tdata

seeds = list(map(int, data[0].removeprefix('seeds: ').strip().split()))
seedt = []
for seed1, l in zip(seeds[::2], seeds[1::2]):
    seedt.append([seed1, seed1, seed1, True])
    seedt.append([seed1+l, seed1, seed1, False])


transformations = {}
key = None
for i in data[1:]:
    if i[0].isalpha():
        i = i.removesuffix(' map:\n')
        key = i 
    elif i[0].isdigit():
        i = list(map(int,i.split()))
        destiny = i[0]
        start = i[1]
        end = i[1] + i[2]
        p1 = [start, destiny, start, True]
        p2 = [end, destiny, start, False]
        transformations[key] = transformations.get(key, []) + [p1,p2]
transformations = list(transformations.values())

transformations = [seedt] + transformations


def sum_ranges(r1, r2):
    if r1[3]:
        destiny1 = r1[1]
    else:
        destiny1 = r1[0]
    if r2[3]:
        destiny2 = 0
    else:
        destiny2 = r2[1]-r2[2]
    
    destiny = destiny1 + destiny2
    return ([r1[0], destiny, r1[0], True], [r2[0], destiny, r1[0], False])

def get_transf(transformations):
    if len(transformations) == 1:
        return transformations
    s = sorted((transformations[0] + transformations[1]), key=lambda x: x[0])
    r = [i for r1, r2 in zip(s[:-1], s[1:]) for i in sum_ranges(r1, r2)]
    return get_transf([r] + transformations[2:])

s = min(get_transf(transformations)[0], key=lambda x:x[1])
print(s)
