import math
with open("inputs/6", "r") as f:
    data = f.readlines()

# with open("tests/6", "r") as f:
#     tdata = f.readlines()
# data = tdata

def calc_winning_games(t,r):
    delta = (t**2-4*-r*-1)**0.5
    x1 = math.floor((-t+delta)/-2)
    x2 = math.ceil((-t-delta)/-2)
    return x2-x1-1


time = list(map(int,data[0].removeprefix('Time: ').strip().split()))
record = list(map(int,data[1].removeprefix('Distance: ').strip().split()))

res = 1
for t,r in zip(time, record):
    w = calc_winning_games(t,r)
    res *= w
print(res)
