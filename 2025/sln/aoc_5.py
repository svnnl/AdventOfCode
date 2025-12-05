TEST = 0
day = __file__.split("\\")[-1][:-3]

path = f"2025/test/test_{day}.txt" if TEST else f"2025/data/{day}.txt"

ranges, ingredients = [
    x.strip().split("\n") for x in open(path, "r").read().split("\n\n")
]

total = 0
for i in ingredients:
    if any(
        int(i) in range(int(r.split("-")[0]), int(r.split("-")[1]) + 1) for r in ranges
    ):
        total += 1

print(f"Answer to Part 1: {total}")

cnt = 0
current = 0

for a, b in sorted([*map(int, r.split("-"))] for r in ranges):
    a = max(a, current + 1)
    cnt += max(0, b - a + 1)
    current = max(current, b)

print(f"Answer to Part 2: {cnt}")
