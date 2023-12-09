from collections import Counter
with open("inputs/7", "r") as f:
    data = f.readlines()

# with open("tests/7", "r") as f:
#     data = f.readlines()

s = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def replace_str_by_index(st):
    return [s.index(c) for c in st]
        
game=[]
for line in data:
    handstr, bid = line.split()
    hand = replace_str_by_index(handstr)
    counter = Counter(hand)
    rank = tuple(-i for i in sorted(counter.values(), reverse=True))
    game.append((rank, int(bid), hand, handstr))
    
game.sort(key=lambda x:(x[0], x[2]))
l = len(game)
print(sum(map(lambda x: (l-x[0])*x[1][1], enumerate(game))))
