import re

patr = re.compile(r'(\d+) red') 
patg = re.compile(r'(\d+) green') 
patb = re.compile(r'(\d+) blue') 

def get_balls(pat, subset):
    return sum(map(int, balls)) if (balls:=pat.findall(subset)) else 0

def calc(data):
    s = 0
    for line in data:
        balls = [(get_balls(patr, subset), get_balls(patg, subset), get_balls(patb, subset)) for subset in line.split(';')]
        mred = max(map(lambda x:x[0], balls))
        mgreen = max(map(lambda x:x[1], balls))
        mblue = max(map(lambda x:x[2], balls))
        s += mred * mblue * mgreen
    print(s)

with open('tests/2a') as f:
    data = f.readlines()
calc(data)

with open('inputs/2a') as f:
    data = f.readlines()
calc(data)
