from collections import Counter
with open("inputs/7", "r") as f:
    data = f.readlines()

# with open("tests/7", "r") as f:
#     data = f.readlines()

# with open("tests/7extra", "r") as f:
#     data = f.readlines()

s = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def replace_str_by_index(st):
    return [s.index(c) for c in st]
        
def do(line):
    hand, bid = line.split()
    oldhand = hand
    handindex = replace_str_by_index(hand)
    counter = Counter(hand)
    m = sorted(counter.items(),key=lambda x:x[1], reverse=True)
    if m[0][0] == 'J' and len(m)>1: sub = m[1][0]
    else: sub = m[0][0]
    hand = hand.replace('J', sub)
    counter = Counter(hand)
    rank = tuple(-i for i in sorted(counter.values(), reverse=True))
    return (rank, int(bid), handindex, hand, oldhand)

game = [do(line) for line in data]
    
game.sort(key=lambda x:(x[0], x[2]))
l = len(game)
print(sum(map(lambda x: (l-x[0])*x[1][1], enumerate(game))))
