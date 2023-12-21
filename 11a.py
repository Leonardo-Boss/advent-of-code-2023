import re
with open("inputs/11", "r") as f:
    data = f.read().splitlines()

with open("tests/11", "r") as f:
    data = f.read().splitlines()

# expand galaxy
expanded_galaxy = []
for i in enumerate(data):
    expanded_galaxy.append(i)
    if '#' in i: continue
    expanded_galaxy.append(i)


# find galaxies
pat = re.compile("#")
galaxies = [(match.start(), i)
for i, line in enumerate(data)
    for match in pat.finditer(line)
]

# calc distances
def manhattan(point1, point2):
    return sum(abs(i-j) for i, j in zip(point1, point2))

r = list((i,j,manhattan(point1,point2))
for i, point1 in enumerate(galaxies, 1)
    for j, point2 in enumerate(galaxies[i:], 2)
        )

print(len(r))
print(r)

test = [0,1,2,3,4,5]
inserts = 0
for j,i in enumerate(test):
    test.insert(i+inserts, -1)
    inserts += 1
    print(len(test))
