import re

with open('inputs/3a') as f:
    data = f.readlines()

lxd = len(data[0])
lyd = len(data)
indexes = (-1,0,1)
indexes = tuple(tuple((i,j) for j in indexes) for i in indexes)

gears = {}
for i, line in enumerate(data):
    for numbers in re.finditer(r'\d+', line):
        for j in range(numbers.start(), numbers.end()):
            ispart=False
            for row in indexes:
                for x,y in row:
                    n = i+x
                    m = j+y
                    if m<=0 and n<=0 or m>=lxd or n>=lyd: continue
                    if data[n][m] == '*':
                        gears[f'{n}-{m}']= (p if (p:=gears.get(f'{n}-{m}')) else []) + [int(numbers.group(0))]
                        break
                else: continue
                break
            else:continue
            break

s=0
for i in gears.values():
    print(i)
    if len(i) == 2:
        s+=i[0]*i[1]
print(s)
