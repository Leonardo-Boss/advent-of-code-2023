import re

with open("inputs/4", "r") as f:
    data = f.readlines()

with open("tests/4", "r") as f:
    tdata = f.readlines()

points = 0
for i in data:
    winning_stuff, your_stuff = i.split(':')[1].split('|')
    winning_stuff = re.sub(r'\s+', ' ', winning_stuff)
    print(winning_stuff)
    winning_stuff = f"({winning_stuff.strip().replace(' ','|')})"
    print(winning_stuff)
    print(your_stuff.strip())
    l = re.findall(fr'(?<!\d){winning_stuff}(?!\d)', your_stuff)
    print(l)
    l = len(l)
    if l:
        print(l)
        point = 2**(l-1)
        print(point)
        points += point
    else: print(0)
    print()
print(points)
