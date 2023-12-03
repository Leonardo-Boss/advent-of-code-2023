import re

with open('inputs/3a') as f:
    data = f.readlines()


def issymbol(c):
    return not(c.isdigit() or c == '.' or c=='\n')

issymbol('#')

lxd = len(data[0])
lyd = len(data)
indexes = (-1,0,1)
indexes = tuple(tuple((i,j) for j in indexes) for i in indexes)
parts = 0

for i, line in enumerate(data):
    for numbers in re.finditer(r'\d+', line):
        for j in range(numbers.start(), numbers.end()):
            ispart=False
            for row in indexes:
                for x,y in row:
                    n = i+x
                    m = j+y
                    if m<=0 and n<=0 or m>=lxd or n>=lyd: continue
                    if issymbol(data[n][m]): ispart = True
            if ispart:
                parts += int(numbers.group(0))
                break
print(parts)
