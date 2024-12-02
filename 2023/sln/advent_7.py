from collections import Counter, defaultdict

TEST = 0
DAY = 7

path = f'test/test_advent_{DAY}.txt' if TEST else f'data/advent_{DAY}.txt'

data = open(path, 'r').read().splitlines()


def play(mapping, part_2):
    ranks = [[] for _ in range(7)]

    for i, hand in enumerate(data):
        cards = [int(x) if x not in mapping.keys() else int(mapping[x])
                 for x in [i for i in hand.split()[0]]]

        bid = int(hand.split()[1])

        cnts = Counter(cards)
        if part_2:
            filtered = {key: value for key, value in cnts.items() if key != 1}
            freq_occ = max(filtered, key=filtered.get, default=None)
            cnts[freq_occ] += cnts[1]
            cnts[1] = 0

        values = list(cnts.values())
        if 5 in values:
            ranks[0].append((cards, bid))
        elif 4 in values:
            ranks[1].append((cards, bid))
        elif all([x in values for x in [3, 2]]):
            ranks[2].append((cards, bid))
        elif 3 in values:
            ranks[3].append((cards, bid))
        elif values.count(2) == 2:
            ranks[4].append((cards, bid))
        elif values.count(2) == 1:
            ranks[5].append((cards, bid))
        else:
            ranks[6].append((cards, bid))

    non_empty_ranks = [l for l in ranks if l]

    final_ranks = sum([sorted(sublist, key=lambda x: tuple(x[0]), reverse=True)
                       for sublist in non_empty_ranks], [])

    sm = 0
    for i, v in enumerate(final_ranks):
        w = v[1] * (len(final_ranks) - i)
        sm += w
    return sm


mapping = {"T": 10,
           "J": 11,
           "Q": 12,
           "K": 13,
           "A": 14}

print(f'Answer to Part 1: {play(mapping, False)}')

mapping["J"] = 1

print(f'Answer to Part 2: {play(mapping, True)}')
