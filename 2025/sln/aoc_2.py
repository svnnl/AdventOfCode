TEST = 0
day = __file__.split("\\")[-1][:-3]

path = f"2025/test/test_{day}.txt" if TEST else f"2025/data/{day}.txt"

data = [i.split("-") for i in open(path, "r").read().split(",")]

invalids = set()
invalids2 = set()


def has_repeating_pattern(s):
    length = len(s)
    for size in range(1, length // 2 + 1):
        pattern = s[:size]
        repeated = pattern * (length // size)
        if repeated == s:
            return True
    return False


for a, b in data:
    for i in range(int(a), int(b) + 1):
        if str(i)[: len(str(i)) // 2] == str(i)[len(str(i)) // 2 :]:
            invalids.add(i)
        elif has_repeating_pattern(str(i)):
            invalids2.add(i)
        else:
            continue

print(f"Answer to Part 1: {sum(invalids)}")
print(f"Answer to Part 2: {sum(invalids | invalids2)}")
