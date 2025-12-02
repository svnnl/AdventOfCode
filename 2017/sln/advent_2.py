with open("../data/advent_2.txt") as f:
    data = [list(map(int, i.split("\t"))) for i in f.read().splitlines()]

print(f"Answer to Part 1: {sum([max(i) - min(i) for i in data])}")
print(
    f"Answer to Part 2: {sum([row[i] // row[j] for row in data for i in range(len(row)) for j in range(len(row)) if row[i] % row[j] == 0 and row[i] != row[j]])}"
)
