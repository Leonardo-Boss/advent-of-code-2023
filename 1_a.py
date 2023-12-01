with open('inputs/input_1_a') as f:
    lines = f.readlines()

def parse_line(line):
    snum = ''.join(list(filter(lambda x:x.isdigit(), line)))
    if snum:
        snum = snum[0]+snum[-1]
        snum = int(snum)
    else: snum = 0
    return snum

print(sum(map(parse_line,lines)))
