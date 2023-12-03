import re

with open('tests/3a') as f:
    data = f.readlines()


def issymbol(c):
    return not(c.isdigit() or c == '.' or c=='\n')

lxd = len(data[0])
lyd = len(data)
indexes = (-1,0,1)
indexes = tuple(tuple((i,j) for j in indexes) for i in indexes)
parts = 0

for i, line in enumerate(data):
    for numbers in re.finditer(r'\*', line):
        j = numbers.start()
        adjecent_nums=[]
        for row in indexes:
            for x,y in row:
                n = i+x
                m = j+y
                if m<=0 and n<=0 or m>=lxd or n>=lyd: continue
                if data[n][m].isdigit(): adjecent_nums.append(data[n][m])
        if len(adjecent_nums)==2:
            parts += adjecent_nums[0]*adjecent_nums[1]
print(parts)
