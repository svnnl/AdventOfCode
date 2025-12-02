import math
from collections import defaultdict

TEST = 0
DAY = 4

path = f"test/test_advent_{DAY}.txt" if TEST else f"data/advent_{DAY}.txt"

data = open(path, "r").read().splitlines()


cards = defaultdict()
instances = [1] * 200


for line in data:
    # Part 1
    card_nmbr, card = line.split(": ")
    card_nmbr = int(card_nmbr.split()[-1])
    winning, nmbrs = [
        list(map(int, x))
        for x in [i.split() for i in card.split(": ")[-1].split(" | ")]
    ]
    len_match = len([x for x in nmbrs if x in winning])
    cards[card_nmbr] = int(math.pow(2, len_match - 1))

    # Part 2
    for i in range(1, len_match + 1):
        try:
            instances[int(card_nmbr) + i] += instances[int(card_nmbr)]
        except IndexError:
            continue

print(f"Answer to Part 1: {sum(cards.values())}")
print(f"Answer to Part 2: {sum(instances[1:])}")
