from collections import defaultdict

with open("../data/advent_7.txt") as f:
    data = f.read().splitlines()

fs = defaultdict(list)

# Create the File Share Dictionary
cd_stack = []
for x in data:
    cmd = x.split(" ")
    if cmd[0] == "$":
        if cmd[1] == "ls":
            continue
        elif cmd[2] == "..":
            cd_stack.pop(-1)
        else:
            cd_stack.append(".".join(cd_stack + [cmd[2]]))
    else:
        if cmd[0] == "dir":
            fs[cd_stack[-1]].append((".".join(cd_stack + [cmd[1]]), 0))
        else:
            fs[cd_stack[-1]].append((".".join(cd_stack + [cmd[1]]), int(cmd[0])))

# Create a Directory structure
directory = defaultdict(list)
for i, v in fs.items():
    for file in v:
        if file[1] == 0:
            directory[i].append(file[0])

# Get Weight per directory
weights = defaultdict(int)
for i, v in fs.items():
    weights[i] = sum([x[1] for x in v])


def calculate_weight(dir):
    for x in directory[dir]:
        weights[dir] += calculate_weight(x)
    return weights[dir]


calculate_weight("/")
print(f"Answer to Part 1: {sum([i for i in weights.values() if i <= 100000])}")
print(
    f'Answer to Part 2: {min(i for i in weights.values() if 70000000 - weights["/"] + i >= 30000000)}'
)
