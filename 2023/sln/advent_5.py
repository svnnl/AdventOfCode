import sys

TEST = 0
DAY = 5

path = f"test/test_advent_{DAY}.txt" if TEST else f"data/advent_{DAY}.txt"

data = open(path, "r").read().split("\n\n")

seeds = [int(i) for i in data[0].split(": ")[-1].split()]


min_seed = sys.maxsize

for seed in seeds:
    for step in data[1:]:
        ranges = [
            list(map(int, i))
            for i in [j.split() for j in step.split(":\n")[-1].split("\n")]
        ]
        for r in ranges:
            if seed in range(r[1], r[1] + r[2]):
                seed = r[0] + (seed - r[1])
                break
    if seed < min_seed:
        min_seed = seed

print(f"Answer to Part 1: {min_seed}")

found = False
start = 10_000_000

while not found:
    seed = start
    if start % 100_000 == 0:
        print(start)
    for i, step in enumerate(reversed(data[1:])):
        ranges = [
            list(map(int, i))
            for i in [j.split() for j in step.split(":\n")[-1].split("\n")]
        ]
        for r in ranges:
            if seed in range(r[0], r[0] + r[2]):
                seed = r[1] + (seed - r[0])
                break
    x = list(range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2))
    if any(seed in i for i in x):
        found = True
        print(f"Answer to Part 2: {start}")
    start += 1
