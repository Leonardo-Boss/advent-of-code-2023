import re
with open("inputs/11", "r") as f:
    data = f.read().splitlines()

# with open("tests/11", "r") as f:
#     data = f.read().splitlines()

# expand galaxy
expanded_galaxy = []
for line in data:
    expanded_galaxy.append(line)
    if '#' in line: continue
    expanded_galaxy.append(line)


for i in reversed(range(len(expanded_galaxy[0]))):
    for j in range(len(expanded_galaxy)):
        if expanded_galaxy[j][i] != '.':
            break
    else:
        for j in range(len(expanded_galaxy)):
            newline = expanded_galaxy[j][0:i] + '.' + expanded_galaxy[j][i:]
            expanded_galaxy[j] = newline


# find galaxies
pat = re.compile("#")
galaxies = [(match.start(), i)
for i, line in enumerate(expanded_galaxy)
    for match in pat.finditer(line)
]

# calc distances
def manhattan(point1, point2):
    return sum(abs(i-j) for i, j in zip(point1, point2))

r = list((i,j,manhattan(point1,point2))
for i, point1 in enumerate(galaxies, 1)
    for j, point2 in enumerate(galaxies[i:], 2)
        )

print(sum(map(lambda x:x[2],r)))
