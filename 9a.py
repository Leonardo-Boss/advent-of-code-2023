with open("inputs/9", "r") as f:
    data = f.readlines()

# with open("tests/9", "r") as f:
#     data = f.readlines()

data = [list(map(int,line.strip().split())) for line in data]

def extrapolate_seq(data, differences):
    diff = [j-i for i,j in zip(data[:-1],data[1:])]
    differences.append(diff)
    if not list(filter(lambda x:x!=0, diff)):
        return differences
    differences = extrapolate_seq(diff, differences)
    differences[-2].append(differences[-2][-1]+differences[-1][-1])
    differences.remove(differences[-1])
    return differences


sum = 0
for i in data:
    differences = [i]
    extrapolate_seq(i, differences)
    differences[-2].append(differences[-2][-1]+differences[-1][-1])
    differences.remove(differences[-1])
    print(differences[-1][-1])

    sum += differences[-1][-1]

print(sum)
