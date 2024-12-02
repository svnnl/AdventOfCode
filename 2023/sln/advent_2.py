from collections import defaultdict
import math

TEST = 0
DAY = 2

path = f'test/test_advent_{DAY}.txt' if TEST else f'data/advent_{DAY}.txt'

data = open(path, 'r').read().splitlines()


games = defaultdict(lambda: defaultdict(list))

for line in data:
    id, game = line.split(': ')
    sets = game.split('; ')
    for s in sets:
        for i in s.split(', '):
            cnt, color = i.split()
            games[int(id.split()[-1])][color].append(int(cnt))

imp = set()

for id, set in games.items():
    if any(value > 12 for value in set['red']) or any(value > 13 for value in set['green']) or any(value > 14 for value in set['blue']):
        imp.add(id)

print(f'Answer to Part 1: {sum(games.keys() - imp)}')

print(
    f"Answer to Part 2: {sum(math.prod([max(v) for v in game.values()]) for game in games.values())}")
