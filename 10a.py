with open("inputs/10", "r") as f:
    data = f.read().splitlines()

# with open("tests/10", "r") as f:
#     data = f.read().splitlines()

def is_edge(x,y):
    return False if x >= 0 and x < len(data[0]) and y >= 0 and y < len(data) else True

def go_pipe(i, j, step, x, y):
    res = -1
    while res == -1:
        match data[x][y]:
            case '|':
                end1, end2 = ((x+1,y),(x-1,y))
            case '-':
                end1, end2 = ((x,y+1),(x,y-1))
            case 'L':
                end1, end2 = ((x,y+1),(x-1,y))
            case 'J':
                end1, end2 = ((x,y-1),(x-1,y))
            case '7':
                end1, end2 = ((x,y-1),(x+1,y))
            case 'F':
                end1, end2 = ((x,y+1),(x+1,y))
            case '.':
                res = False
                break
            case 'S':
                res = step
                break
            case _:
                res = False
                break
        ends = (end1,end2)
        if (i,j) not in ends:
            res = False
            break
        next = list(filter(lambda x: (i,j) != x, ends))
        next = next[0]
        if is_edge(*next):
            res = False
            break
        i = x
        j = y
        step += 1
        x, y = next
    return res

i,j = 0,0
for i, line in enumerate(data):
    j = line.rfind('S')
    if j < 0: continue
    break

for x,y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    x = i+x
    y = j+y
    if is_edge(x,y):continue
    if (l:=go_pipe(i,j, 1,x,y)):
        print(l//2)
        break
