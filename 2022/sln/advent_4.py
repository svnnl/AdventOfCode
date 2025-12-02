with open("../data/advent_4.txt") as f:
    data = f.read().splitlines()

c = 0
for line in data:
    i, j = line.split(",")
    if (
        int(i.split("-")[0]) <= int(j.split("-")[0])
        and int(i.split("-")[1]) >= int(j.split("-")[1])
    ) or (
        int(j.split("-")[0]) <= int(i.split("-")[0])
        and int(j.split("-")[1]) >= int(i.split("-")[1])
    ):
        c += 1

print(f"Answer to Part 1: {c}")

c = 0
for line in data:
    i, j = line.split(",")
    i_min, i_max = [int(i) for i in i.split("-")]
    j_min, j_max = [int(i) for i in j.split("-")]

    if any(k in range(i_min, i_max + 1) for k in range(j_min, j_max + 1)) or any(
        x in range(j_min, j_max + 1) for x in range(i_min, i_max + 1)
    ):
        c += 1

print(f"Answer to Part 2: {c}")
