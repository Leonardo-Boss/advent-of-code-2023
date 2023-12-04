import re

with open("inputs/4", "r") as f:
    data = f.readlines()

with open("tests/4", "r") as f:
    tdata = f.readlines()


def get_cards(card):
    card_id, numbers = card.split(':')
    next_card_id = int(card_id.removeprefix('Card '))
    winning_stuff, your_stuff = numbers.split('|')
    winning_stuff = re.sub(r'\s+', ' ', winning_stuff)
    winning_stuff = f"({winning_stuff.strip().replace(' ','|')})"
    l = len(re.findall(fr'(?<!\d){winning_stuff}(?!\d)', your_stuff))
    cards = 1
    for i in range(next_card_id, next_card_id+l):
        cards += get_cards(data[i])
    return cards


cards = 0
for i in data:
    cards += get_cards(i)
print(cards)
