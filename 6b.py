import math
with open("inputs/6", "r") as f:
    data = f.readlines()

# with open("tests/6", "r") as f:
#     tdata = f.readlines()
# data = tdata

time = int(data[0].removeprefix('Time: ').strip().replace(' ',''))
record = int(data[1].removeprefix('Distance: ').strip().replace(' ',''))

def calc_winning_games(t,r):
    delta = (t**2-4*-r*-1)**0.5
    x1 = math.floor((-t+delta)/-2)
    x2 = math.ceil((-t-delta)/-2)
    return x2-x1-1

print(calc_winning_games(time, record))
