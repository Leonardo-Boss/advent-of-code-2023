import re
from tqdm import tqdm
from itertools import tee
from typing_extensions import Iterator

with open("inputs/12", "r") as f:
    data = f.read().splitlines()

# with open("tests/12", "r") as f:
#     data = f.read().splitlines()


res = []
def get_iter(line,iterator:Iterator[re.Match[str]],res,bar):
    bar.update()
    try:
        match = next(iterator)
    except StopIteration:
        res.append(line)
        return
    index = match.start()
    nextline1 = line[0:index] + '.' + line[index+1:]
    nextline2 = line[0:index] + '#' + line[index+1:]
    iterator1, iterator2 = tee(iterator)
    get_iter(nextline1, iterator1, res, bar)
    get_iter(nextline2, iterator2, res, bar)

pat = re.compile(r'\?')
def bruteregex(data,bar):
    res = []
    for line in data:
        all = pat.finditer(line)
        resi=[]
        get_iter(line, all, resi,bar)
        res.append(resi)
    bar.close()
    return res

check_pat = re.compile(r'\.+')
def check(res):
    final=[]
    for r in tqdm(res, desc='checking'):
        num=0
        nums = r[0].split()[1].split(',')
        for s in r:
            s=s.split()[0]
            arr=list(map(lambda x:str(len(x)), check_pat.sub(' ',s).split()))
            if arr != nums: continue
            num += 1
        final.append(num)
    return final

print(sum(check(bruteregex(data,tqdm(desc='getting options')))))
