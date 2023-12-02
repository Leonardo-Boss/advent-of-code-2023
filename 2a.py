import re

mred = 12
mgreen = 13
mblue = 14

patr = re.compile(r'(\d+) red') 
patg = re.compile(r'(\d+) green') 
patb = re.compile(r'(\d+) blue') 

def calc(data):
    s = 0
    for line in data:
        for subset in line.split(';'):
            print(subset)
            red = sum(map(int, redm)) if (redm:=patr.findall(subset)) else 0
            green = sum(map(int, greenm)) if (greenm:=patg.findall(subset)) else 0
            blue = sum(map(int, bluem)) if (bluem:=patb.findall(subset)) else 0
            if red > mred or green > mgreen or blue > mblue:
                break
        else:
            g = line.split(':')[0].removeprefix('Game ')
            print(g)
            s += int(g)
    print(s)

with open('tests/2a') as f:
    data = f.readlines()
calc(data)

with open('inputs/2a') as f:
    data = f.readlines()
calc(data)
